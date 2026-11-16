-- Track registration transactions without storing private keys.

CREATE TABLE blockchain_transactions (
    transaction_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    transaction_hash TEXT NOT NULL UNIQUE,
    operation TEXT NOT NULL,
    status TEXT NOT NULL
        CHECK (status IN ('submitted', 'confirmed', 'failed')),
    snake_id TEXT REFERENCES snakes (snake_id)
);