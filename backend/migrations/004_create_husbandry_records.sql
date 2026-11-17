-- Store off-chain husbandry records with their original authors.
-- Keeper changes must not reassign these records.

CREATE TABLE growth_records (
    record_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    snake_id TEXT NOT NULL REFERENCES snakes (snake_id),
    created_by TEXT NOT NULL REFERENCES participants (participant_id),
    record_date DATE NOT NULL,
    weight_g NUMERIC NOT NULL,
    length_cm NUMERIC,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE shedding_records (
    record_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    snake_id TEXT NOT NULL REFERENCES snakes (snake_id),
    created_by TEXT NOT NULL REFERENCES participants (participant_id),
    record_date DATE NOT NULL,
    outcome TEXT NOT NULL
        CHECK (outcome ~ '[^[:space:]]'),
    follow_up TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE feeding_records (
    record_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    snake_id TEXT NOT NULL REFERENCES snakes (snake_id),
    created_by TEXT NOT NULL REFERENCES participants (participant_id),
    record_date DATE NOT NULL,
    food TEXT NOT NULL
        CHECK (food ~ '[^[:space:]]'),
    feeding_outcome TEXT NOT NULL
        CHECK (feeding_outcome ~ '[^[:space:]]'),
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE health_records (
    record_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    snake_id TEXT NOT NULL REFERENCES snakes (snake_id),
    created_by TEXT NOT NULL REFERENCES participants (participant_id),
    record_date DATE NOT NULL,
    event TEXT NOT NULL
        CHECK (event ~ '[^[:space:]]'),
    follow_up TEXT,
    status TEXT NOT NULL
        CHECK (status ~ '[^[:space:]]'),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);