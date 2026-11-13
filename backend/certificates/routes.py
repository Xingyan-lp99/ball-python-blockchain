from contextlib import contextmanager
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, File, Form, HTTPException, Path, Request, Response, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from blockchain.transactions import CHAIN_ERRORS, TransactionProblem
from certificates import service, histories
from certificates.local_chain import get_certificate_chain, get_versioned_certificate_chain, CertificatePreflightError
from snake_registry.local_chain import ChainConflict, ChainStale
from certificates.models import Certificate
from certificates.storage import original_path, read_pdf
from database import get_session
from identity import get_current_lab_id
from snake_registry.models import Snake
from snake_registry.schemas import RegistrationSubmit

router = APIRouter(tags=["certificates"])
DatabaseSession = Annotated[Session, Depends(get_session)]
CurrentLab = Annotated[str, Depends(get_current_lab_id)]
VersionNumber = Annotated[int, Path(ge=1, le=2)]


def view(session, row):
    return histories.metadata_view(session, row, get_certificate_chain, get_versioned_certificate_chain)


def factory_for(session, row):
    return histories.bound_factory(session, row, get_certificate_chain, get_versioned_certificate_chain)


@contextmanager
def api_errors():
    try:
        yield
    except TransactionProblem as error:
        detail = {"code": error.code, "message": error.detail} if error.code else error.detail
        raise HTTPException(status_code=error.status_code, detail=detail) from None
    except CertificatePreflightError as error:
        raise HTTPException(status_code=409, detail={"code": error.code, "message": error.detail}) from None
    except (ChainStale, ChainConflict):
        raise HTTPException(status_code=409, detail="Selected deployment/series evidence is stale or conflicts; history is retained") from None
    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="Database unavailable; query the selected certificate before retrying") from None
    except CHAIN_ERRORS:
        raise HTTPException(status_code=503, detail="Local deployment or document storage unavailable") from None


async def upload_fields(request: Request):
    form = await request.form()
    if set(form) - {"certificate_id", "snake_id", "file"} or any(len(form.getlist(key)) != 1 for key in form):
        raise HTTPException(status_code=422, detail="Only certificate_id, snake_id and one PDF file are accepted")


async def verification_fields(request: Request):
    form = await request.form()
    if set(form) != {"file"} or len(form.getlist("file")) != 1:
        raise HTTPException(status_code=422, detail="Only one independently uploaded PDF file is accepted")


@router.post("/certificates", dependencies=[Depends(upload_fields)])
def upload_certificate(
    response: Response, session: DatabaseSession, lab_id: CurrentLab,
    certificate_id: Annotated[str, Form()], snake_id: Annotated[str, Form()],
    file: Annotated[UploadFile, File()],
):
    with api_errors():
        row, created = service.upload_v1(session, certificate_id, snake_id, read_pdf(file), file.filename or "document.pdf", lab_id, get_certificate_chain)
        response.status_code = 201 if created else 200
        return view(session, row)


@router.get("/snakes/{snake_id:path}/certificates")
def snake_certificates(snake_id: str, session: DatabaseSession):
    with api_errors():
        snake = session.scalar(select(Snake).where(Snake.snake_id == snake_id.strip()))
        if snake is None:
            raise TransactionProblem(404, "Snake database profile not found")
        certificates = session.scalars(select(Certificate).where(Certificate.snake_id == snake.id).order_by(Certificate.created_at)).all()
        result = []
        for item in certificates:
            catalog = histories.catalog(session, item.certificate_id, get_certificate_chain, get_versioned_certificate_chain)
            result.append(next(version for history in catalog["histories"] for version in history["versions"]
                               if version["history_id"] == catalog["default_history_id"] and version["version"] == catalog["default_version"]))
        return result


@router.post("/certificates/{certificate_id:path}/versions/{version_number}/issuance")
def issue_certificate(certificate_id: str, version_number: VersionNumber, data: RegistrationSubmit, session: DatabaseSession, lab_id: CurrentLab, history_id: UUID | None = None):
    with api_errors():
        row = service.selected_certificate(session, certificate_id, version_number, history_id)
        return service.issue_v1(session, row, lab_id, factory_for(session, row))


@router.get("/certificates/{certificate_id:path}/versions/{version_number}/issuance")
def certificate_issuance(certificate_id: str, version_number: VersionNumber, session: DatabaseSession, history_id: UUID | None = None):
    with api_errors():
        row = service.selected_certificate(session, certificate_id, version_number, history_id)
        return service.issuance_state(session, row, factory_for(session, row))


@router.get("/certificates/{certificate_id:path}/versions/{version_number}/file")
def download_certificate(certificate_id: str, version_number: VersionNumber, session: DatabaseSession, history_id: UUID | None = None):
    with api_errors():
        row = service.selected_certificate(session, certificate_id, version_number, history_id)
        path = original_path(row[4].storage_key)
        if not path.is_file():
            raise TransactionProblem(503, "Original PDF is unavailable in document storage")
        return FileResponse(path, media_type="application/pdf", filename=f"certificate-{row[1].id}-v{version_number}.pdf")


@router.post("/certificates/{certificate_id:path}/versions/{version_number}/verification", dependencies=[Depends(verification_fields)])
def verify_certificate(certificate_id: str, version_number: VersionNumber, session: DatabaseSession, file: Annotated[UploadFile, File()], history_id: UUID | None = None):
    with api_errors():
        row = service.selected_certificate(session, certificate_id, version_number, history_id)
        return service.verify_file(session, row, read_pdf(file), factory_for(session, row))


@router.post("/certificates/{certificate_id:path}/versions/{version_number}/verification/stored")
def verify_platform_certificate(certificate_id: str, version_number: VersionNumber, data: RegistrationSubmit, session: DatabaseSession, history_id: UUID | None = None):
    with api_errors():
        row = service.selected_certificate(session, certificate_id, version_number, history_id)
        return service.verify_stored_file(session, row, factory_for(session, row))


@router.get("/certificates/{certificate_id:path}/versions/{version_number}")
def certificate_metadata(certificate_id: str, version_number: VersionNumber, session: DatabaseSession, history_id: UUID | None = None):
    with api_errors():
        row = service.selected_certificate(session, certificate_id, version_number, history_id)
        return view(session, row)


@router.get("/certificates/{certificate_id:path}/histories")
def certificate_histories(certificate_id: str, session: DatabaseSession):
    with api_errors():
        return histories.catalog(session, certificate_id, get_certificate_chain, get_versioned_certificate_chain)


@router.post("/certificates/{certificate_id:path}/histories")
def initialize_versioned_history(certificate_id: str, data: RegistrationSubmit, response: Response, session: DatabaseSession, lab_id: CurrentLab):
    with api_errors():
        row, created = histories.create_versioned_history(session, certificate_id, lab_id, get_certificate_chain, get_versioned_certificate_chain)
        response.status_code = 201 if created else 200
        return view(session, row)


@router.post("/certificates/{certificate_id:path}/histories/{history_id}/versions", dependencies=[Depends(verification_fields)])
def upload_next_version(certificate_id: str, history_id: UUID, response: Response, session: DatabaseSession, lab_id: CurrentLab, file: Annotated[UploadFile, File()]):
    with api_errors():
        row, created = histories.upload_next_version(session, certificate_id, history_id, read_pdf(file), file.filename or "version.pdf", lab_id, get_certificate_chain, get_versioned_certificate_chain)
        response.status_code = 201 if created else 200
        return view(session, row)
