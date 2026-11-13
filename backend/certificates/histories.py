"""Explicit deployment histories: never splice old V1 evidence into a new registry."""
import hashlib
from pathlib import Path

from sqlalchemy import select

from blockchain.transactions import CHAIN_ERRORS, TransactionProblem, transaction_lock
from certificates import service
from certificates.models import Certificate, CertificateHistory, CertificateVersion, StoredFile
from certificates.storage import original_path, save_original
from snake_registry.local_chain import ChainConflict, ChainStale


def bound_factory(session, row, legacy_factory, versioned_factory):
    history = session.get(CertificateHistory, row[1].history_id)

    def factory():
        chain = versioned_factory() if history.registry_kind == "versioned" else legacy_factory()
        if history.contract_address is not None and (
            history.chain_id != chain.chain_id or history.contract_address.lower() != chain.address.lower()
            or history.instance_id != chain.instance_id
        ):
            raise ChainStale
        return chain
    return factory


def metadata_view(session, row, legacy_factory, versioned_factory):
    factory = bound_factory(session, row, legacy_factory, versioned_factory)
    state = service.issuance_state(session, row, factory)
    history = session.get(CertificateHistory, row[1].history_id)
    result = service.metadata(row, state)
    result["issuance"] = state.model_dump()
    result.update(history_id=str(history.id), registry_kind=history.registry_kind,
                  history_contract_address=history.contract_address, history_instance_id=history.instance_id,
                  version_status="unknown", latest_version=None)
    if state.status == "confirmed" and state.chain_check == "verified":
        try:
            chain = factory()
            chain.validate_scope()
            result.update(service.version_information(chain, row[0].certificate_id, row[1].version_number))
        except (ChainStale, ChainConflict, *CHAIN_ERRORS):
            pass
    return result


def catalog(session, certificate_id, legacy_factory, versioned_factory):
    certificate = session.scalar(select(Certificate).where(Certificate.certificate_id == certificate_id.strip()))
    if certificate is None:
        raise TransactionProblem(404, "Certificate series not found")
    histories = session.scalars(select(CertificateHistory).where(CertificateHistory.certificate_id == certificate.id)
                                .order_by(CertificateHistory.created_at, CertificateHistory.id)).all()
    entries, confirmed = [], []
    for history in histories:
        numbers = session.scalars(select(CertificateVersion.version_number).where(CertificateVersion.history_id == history.id)
                                  .order_by(CertificateVersion.version_number)).all()
        versions = [metadata_view(session, service.selected_certificate(session, certificate_id, n, history.id), legacy_factory, versioned_factory) for n in numbers]
        entries.append({"history_id": str(history.id), "registry_kind": history.registry_kind,
                        "contract_address": history.contract_address, "instance_id": history.instance_id,
                        "versions": versions})
        confirmed += [item for item in versions if item["issuance"]["status"] == "confirmed" and item["version_status"] != "unknown"]
    preferred = confirmed[-1] if confirmed else entries[0]["versions"][0]
    return {"certificate_id": certificate_id, "histories": entries,
            "default_history_id": preferred["history_id"], "default_version": preferred["version"]}


def create_versioned_history(session, certificate_id, lab_id, legacy_factory, versioned_factory):
    if lab_id != "LAB001":
        raise TransactionProblem(403, "Only the original demo laboratory may initialize a new deployment history")
    with transaction_lock(session):
        old = service.selected_certificate(session, certificate_id)
        if old[3].lab_id != lab_id:
            raise TransactionProblem(403, "Certificate series belongs to another laboratory")
        factory = bound_factory(session, old, legacy_factory, versioned_factory)
        if service.reconcile(session, old, service.latest_attempt(session, old[1]), factory()).status != "confirmed":
            raise TransactionProblem(409, "Legacy V1 must be confirmed and verified before creating the separate history")
        with original_path(old[4].storage_key).open("rb") as source:
            digest = hashlib.sha256(source.read()).digest()
        if digest != old[1].file_hash:
            raise TransactionProblem(409, "Stored original V1 bytes differ from the existing evidence; no reissuance allowed")
        chain = versioned_factory()
        chain.validate_scope()
        if chain.manager.lower() != old[1].issuer_address.lower():
            raise TransactionProblem(403, "New deployment signer must remain the original laboratory")
        existing = session.scalar(select(CertificateHistory).where(CertificateHistory.certificate_id == old[0].id,
                                  CertificateHistory.registry_kind == "versioned", CertificateHistory.instance_id == chain.instance_id))
        if existing:
            return service.selected_certificate(session, certificate_id, 1, existing.id), False
        history = CertificateHistory(certificate_id=old[0].id, registry_kind="versioned", chain_id=chain.chain_id,
                                     contract_address=chain.address, instance_id=chain.instance_id)
        session.add(history)
        session.flush()
        version = CertificateVersion(certificate_id=old[0].id, history_id=history.id, version_number=1,
                                     file_id=old[4].id, file_hash=digest, hash_algorithm="sha256", issuer_address=old[1].issuer_address)
        session.add(version)
        session.commit()
        return service.selected_certificate(session, certificate_id, 1, history.id), True


def upload_next_version(session, certificate_id, history_id, content, filename, lab_id, legacy_factory, versioned_factory):
    if lab_id != "LAB001":
        raise TransactionProblem(403, "Only the original demo laboratory may append")
    with transaction_lock(session):
        first = service.selected_certificate(session, certificate_id, 1, history_id)
        history = session.get(CertificateHistory, first[1].history_id)
        if history.registry_kind != "versioned":
            raise TransactionProblem(409, "Legacy deployment supports only V1; initialize a separate new deployment history")
        if first[3].lab_id != lab_id:
            raise TransactionProblem(403, "Series laboratory is immutable")
        chain = bound_factory(session, first, legacy_factory, versioned_factory)()
        chain.validate_scope()
        record = chain.record(certificate_id, 1)
        if record is None:
            raise TransactionProblem(409, "Issue and confirm V1 on this NEW deployment before uploading V2")
        chain.assert_record(service.subject_for(first), record)
        if chain.manager.lower() != record["issuer_address"].lower():
            raise TransactionProblem(403, "Only the original issuer can append")
        existing = session.scalar(select(CertificateVersion).where(CertificateVersion.history_id == history.id,
                                                                   CertificateVersion.version_number == 2))
        digest = hashlib.sha256(content).digest()
        if existing:
            if existing.file_hash != digest:
                raise TransactionProblem(409, "V2 already saved; original version bytes cannot be replaced")
            return service.selected_certificate(session, certificate_id, 2, history.id), False
        latest = chain.latest_version(certificate_id)
        if latest != 1:
            raise TransactionProblem(409, "This iteration only appends V2 to an existing on-chain V1")
        subject = service.subject_for(first)
        from certificates.local_chain import CertificateSubject
        chain.assert_can_issue(CertificateSubject(subject.certificate_id, subject.snake_id, subject.issuer_address, digest, 2))
        key, digest = save_original(content)
        stored = StoredFile(storage_key=key, original_filename=Path(filename.replace("\\", "/")).name,
                            media_type="application/pdf", size_bytes=len(content), content_hash=digest)
        session.add(stored)
        session.flush()
        version = CertificateVersion(certificate_id=first[0].id, history_id=history.id, version_number=2,
                                     file_id=stored.id, file_hash=digest, hash_algorithm="sha256", issuer_address=first[1].issuer_address)
        session.add(version)
        session.commit()
        return service.selected_certificate(session, certificate_id, 2, history.id), True
