CREATE TABLE laboratories (
    id uuid PRIMARY KEY,
    lab_id text NOT NULL UNIQUE,
    display_name text NOT NULL
);
CREATE TABLE files (
    id uuid PRIMARY KEY,
    storage_key text NOT NULL UNIQUE,
    original_filename text NOT NULL,
    media_type text NOT NULL CHECK (media_type = 'application/pdf'),
    size_bytes bigint NOT NULL CHECK (size_bytes > 0),
    content_hash bytea NOT NULL CHECK (octet_length(content_hash) = 32),
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE certificates (
    id uuid PRIMARY KEY,
    certificate_id text NOT NULL UNIQUE CHECK (length(btrim(certificate_id)) > 0),
    snake_id uuid NOT NULL REFERENCES snakes(id),
    laboratory_id uuid NOT NULL REFERENCES laboratories(id),
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX ix_certificates_snake ON certificates(snake_id);
CREATE TABLE certificate_versions (
    id uuid PRIMARY KEY,
    certificate_id uuid NOT NULL REFERENCES certificates(id),
    version_number integer NOT NULL CHECK (version_number > 0),
    file_id uuid NOT NULL REFERENCES files(id),
    file_hash bytea NOT NULL CHECK (octet_length(file_hash) = 32),
    hash_algorithm text NOT NULL CHECK (hash_algorithm = 'sha256'),
    issuer_address varchar(42) NOT NULL,
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (certificate_id, version_number)
);
CREATE TABLE certificate_issuance_attempts (
    id uuid PRIMARY KEY,
    version_id uuid NOT NULL REFERENCES certificate_versions(id),
    chain_id bigint NOT NULL,
    contract_address varchar(42) NOT NULL,
    instance_id varchar(66) NOT NULL,
    manager_address varchar(42) NOT NULL,
    nonce bigint,
    gas_price bigint,
    start_block bigint NOT NULL,
    transaction_hash varchar(66),
    status text NOT NULL DEFAULT 'prepared' CHECK (status IN ('prepared','submitted','confirmed','failed')),
    block_number bigint,
    block_hash varchar(66),
    failure_code text,
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (status <> 'confirmed' OR (transaction_hash IS NOT NULL AND block_number IS NOT NULL AND block_hash IS NOT NULL)),
    UNIQUE (chain_id, instance_id, transaction_hash)
);
CREATE INDEX ix_certificate_attempt_version ON certificate_issuance_attempts(version_id, created_at DESC);
