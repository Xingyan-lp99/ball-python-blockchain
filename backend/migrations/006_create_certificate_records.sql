-- Laboratory profiles remain separate from staff login accounts.

CREATE TABLE laboratories (
    laboratory_id TEXT PRIMARY KEY
        CHECK (laboratory_id <> ''),

    participant_id TEXT NOT NULL UNIQUE
        REFERENCES participants (participant_id),

    name TEXT NOT NULL
        CHECK (name ~ '[^[:space:]]'),

    testing_direction TEXT
);

-- Each independent report belongs to its own series.

CREATE TABLE certificate_series (
    series_id TEXT PRIMARY KEY
        CHECK (series_id <> ''),

    snake_id TEXT NOT NULL
        REFERENCES snakes (snake_id),

    laboratory_id TEXT NOT NULL
        REFERENCES laboratories (laboratory_id),

    title TEXT NOT NULL
        CHECK (title ~ '[^[:space:]]')
);

-- Revisions add rows; earlier files and evidence remain preserved.

CREATE TABLE certificate_versions (
    version_id TEXT PRIMARY KEY
        CHECK (version_id <> ''),

    series_id TEXT NOT NULL
        REFERENCES certificate_series (series_id),

    version_number INTEGER NOT NULL
        CHECK (version_number > 0),

    previous_version_id TEXT
        REFERENCES certificate_versions (version_id),

    file_reference TEXT NOT NULL
        CHECK (file_reference ~ '[^[:space:]]'),

    file_hash TEXT NOT NULL
        CHECK (file_hash ~ '^[0-9a-f]{64}$'),

    issuer_address TEXT NOT NULL
        CHECK (issuer_address ~ '^0x[0-9a-fA-F]{40}$'),

    status SMALLINT
        CHECK (status IN (1, 2)),

    issued_at TIMESTAMPTZ,

    UNIQUE (series_id, version_number),

    CHECK (
        (version_number = 1 AND previous_version_id IS NULL)
        OR
        (version_number > 1 AND previous_version_id IS NOT NULL)
    )
);

ALTER TABLE blockchain_transactions
    ADD COLUMN version_id TEXT
        REFERENCES certificate_versions (version_id);
