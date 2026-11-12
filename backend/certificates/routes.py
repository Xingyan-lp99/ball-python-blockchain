from contextlib import contextmanager
from typing import Annotated

from fastapi import APIRouter, Depends, File, Form, HTTPException, Request, Response, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from blockchain.transactions import CHAIN_ERRORS, TransactionProblem
from certificates import service
from certificates.local_chain import get_certificate_chain
from certificates.models import Certificate
from certificates.storage import original_path, read_pdf
from database import get_session
from identity import get_current_lab_id
from snake_registry.models import Snake
from snake_registry.schemas import RegistrationSubmit

router = APIRouter(tags=["certificates"])
DatabaseSession = Annotated[Session, Depends(get_session)]
CurrentLab = Annotated[str, Depends(get_current_lab_id)]


@contextmanager
def api_errors():
    try:
        yield
    except TransactionProblem as error:
        detail = {"code": error.code, "message": error.detail} if error.code else error.detail
        raise HTTPException(status_code=error.status_code, detail=detail) from None
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
        return service.metadata(row, service.issuance_state(session, row, get_certificate_chain))


@router.get("/snakes/{snake_id:path}/certificates")
def snake_certificates(snake_id: str, session: DatabaseSession):
    with api_errors():
        snake = session.scalar(select(Snake).where(Snake.snake_id == snake_id.strip()))
        if snake is None:
            raise TransactionProblem(404, "Snake database profile not found")
        certificates = session.scalars(select(Certificate).where(Certificate.snake_id == snake.id).order_by(Certificate.created_at)).all()
        result = []
        for item in certificates:
            row = service.selected_certificate(session, item.certificate_id)
            result.append(service.metadata(row, service.issuance_state(session, row, get_certificate_chain)))
        return result


@router.post("/certificates/{certificate_id:path}/versions/1/issuance")
def issue_certificate(certificate_id: str, data: RegistrationSubmit, session: DatabaseSession, lab_id: CurrentLab):
    with api_errors():
        return service.issue_v1(session, service.selected_certificate(session, certificate_id), lab_id, get_certificate_chain)


@router.get("/certificates/{certificate_id:path}/versions/1/issuance")
def certificate_issuance(certificate_id: str, session: DatabaseSession):
    with api_errors():
        return service.issuance_state(session, service.selected_certificate(session, certificate_id), get_certificate_chain)


@router.get("/certificates/{certificate_id:path}/versions/1/file")
def download_certificate(certificate_id: str, session: DatabaseSession):
    with api_errors():
        row = service.selected_certificate(session, certificate_id)
        path = original_path(row[4].storage_key)
        if not path.is_file():
            raise TransactionProblem(503, "Original PDF is unavailable in document storage")
        return FileResponse(path, media_type="application/pdf", filename=f"certificate-{row[1].id}-v1.pdf")


@router.post("/certificates/{certificate_id:path}/versions/1/verification", dependencies=[Depends(verification_fields)])
def verify_certificate(certificate_id: str, session: DatabaseSession, file: Annotated[UploadFile, File()]):
    with api_errors():
        return service.verify_file(session, service.selected_certificate(session, certificate_id), read_pdf(file), get_certificate_chain)


@router.post("/certificates/{certificate_id:path}/versions/1/verification/stored")
def verify_platform_certificate(certificate_id: str, data: RegistrationSubmit, session: DatabaseSession):
    with api_errors():
        return service.verify_stored_file(session, service.selected_certificate(session, certificate_id), get_certificate_chain)


@router.get("/certificates/{certificate_id:path}/versions/1")
def certificate_metadata(certificate_id: str, session: DatabaseSession):
    with api_errors():
        row = service.selected_certificate(session, certificate_id)
        return service.metadata(row, service.issuance_state(session, row, get_certificate_chain))
