from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import BigInteger, DateTime, ForeignKey, LargeBinary, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from snake_registry.models import Base


class Laboratory(Base):
    __tablename__ = "laboratories"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    lab_id: Mapped[str] = mapped_column(Text, unique=True)
    display_name: Mapped[str] = mapped_column(Text)


class StoredFile(Base):
    __tablename__ = "files"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    storage_key: Mapped[str] = mapped_column(Text, unique=True)
    original_filename: Mapped[str] = mapped_column(Text)
    media_type: Mapped[str] = mapped_column(Text, default="application/pdf")
    size_bytes: Mapped[int] = mapped_column(BigInteger)
    content_hash: Mapped[bytes] = mapped_column(LargeBinary)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class Certificate(Base):
    __tablename__ = "certificates"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    certificate_id: Mapped[str] = mapped_column(Text, unique=True)
    snake_id: Mapped[UUID] = mapped_column(ForeignKey("snakes.id"))
    laboratory_id: Mapped[UUID] = mapped_column(ForeignKey("laboratories.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class CertificateVersion(Base):
    __tablename__ = "certificate_versions"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    certificate_id: Mapped[UUID] = mapped_column(ForeignKey("certificates.id"))
    version_number: Mapped[int] = mapped_column(default=1)
    file_id: Mapped[UUID] = mapped_column(ForeignKey("files.id"))
    file_hash: Mapped[bytes] = mapped_column(LargeBinary)
    hash_algorithm: Mapped[str] = mapped_column(Text, default="sha256")
    issuer_address: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class IssuanceAttempt(Base):
    __tablename__ = "certificate_issuance_attempts"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    version_id: Mapped[UUID] = mapped_column(ForeignKey("certificate_versions.id"))
    chain_id: Mapped[int] = mapped_column(BigInteger)
    contract_address: Mapped[str]
    instance_id: Mapped[str]
    manager_address: Mapped[str]
    nonce: Mapped[int | None] = mapped_column(BigInteger)
    gas_price: Mapped[int | None] = mapped_column(BigInteger)
    start_block: Mapped[int] = mapped_column(BigInteger)
    transaction_hash: Mapped[str | None]
    status: Mapped[str] = mapped_column(default="prepared")
    block_number: Mapped[int | None] = mapped_column(BigInteger)
    block_hash: Mapped[str | None]
    failure_code: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
