CREATE TABLE snake_registration_attempts (
    id uuid PRIMARY KEY,
    snake_id uuid NOT NULL REFERENCES snakes(id),
    chain_id bigint NOT NULL,
    contract_address varchar(42) NOT NULL,
    instance_id varchar(66) NOT NULL,
    manager_address varchar(42) NOT NULL,
    nonce bigint,
    gas_price bigint,
    start_block bigint NOT NULL,
    transaction_hash varchar(66),
    status text NOT NULL DEFAULT 'prepared',
    block_number bigint,
    block_hash varchar(66),
    failure_code text,
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT ck_registration_attempt_status CHECK (status IN ('prepared', 'submitted', 'confirmed', 'failed')),
    CONSTRAINT ck_registration_confirmed CHECK (
        status <> 'confirmed' OR (transaction_hash IS NOT NULL AND block_number IS NOT NULL AND block_hash IS NOT NULL)
    ),
    CONSTRAINT uq_registration_transaction UNIQUE (chain_id, instance_id, transaction_hash)
);
CREATE INDEX ix_registration_attempt_snake ON snake_registration_attempts(snake_id, created_at DESC);
