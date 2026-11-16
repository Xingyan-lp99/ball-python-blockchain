-- Demo step 1: store participants and off-chain snake profiles.
-- These tables connect profile authorship and keeper references to local accounts.

CREATE TABLE participants (
    participant_id TEXT PRIMARY KEY,
    display_name TEXT NOT NULL,
    wallet_address TEXT NOT NULL
        CHECK (wallet_address ~ '^0x[0-9a-fA-F]{40}$')
);

CREATE UNIQUE INDEX participants_wallet_address_unique
    ON participants (LOWER(wallet_address));

CREATE TABLE snakes (
    snake_id TEXT PRIMARY KEY
        CHECK (snake_id <> ''),

    breeder_id TEXT NOT NULL
        REFERENCES participants (participant_id),

    current_keeper_id TEXT
        REFERENCES participants (participant_id),

    breeder_internal_id TEXT NOT NULL
        CHECK (breeder_internal_id ~ '[^[:space:]]'),

    nickname TEXT,

    species TEXT NOT NULL
        CHECK (species ~ '[^[:space:]]'),

    sex TEXT,

    date_of_birth DATE NOT NULL,

    introduction TEXT,

    genetic_description TEXT NOT NULL
        CHECK (genetic_description ~ '[^[:space:]]'),

    sire_description TEXT,
    dam_description TEXT,

    photo_reference TEXT NOT NULL
        CHECK (photo_reference ~ '[^[:space:]]'),

    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);