-- Keep Sepolia pet profiles and transaction checkpoints separate from Anvil data.
CREATE TABLE IF NOT EXISTS public.sepolia_pet_registrations (
    snake_id TEXT PRIMARY KEY CHECK (snake_id <> ''),
    participant_id TEXT NOT NULL REFERENCES public.participants (participant_id),
    species TEXT NOT NULL CHECK (species ~ '[^[:space:]]' AND char_length(species) <= 100),
    sex TEXT NOT NULL CHECK (sex ~ '[^[:space:]]'),
    date_of_birth DATE NOT NULL,
    genetic_description TEXT,
    nickname TEXT,
    introduction TEXT,
    sire_description TEXT,
    dam_description TEXT,
    photo_reference TEXT NOT NULL CHECK (photo_reference ~ '[^[:space:]]'),
    contract_address TEXT NOT NULL CHECK (contract_address ~ '^0x[0-9a-fA-F]{40}$'),
    transaction_hash TEXT NOT NULL UNIQUE CHECK (transaction_hash ~ '^0x[0-9a-fA-F]{64}$'),
    transaction_nonce BIGINT NOT NULL CHECK (transaction_nonce >= 0),
    transaction_status TEXT NOT NULL CHECK (
        transaction_status IN ('prepared', 'submitted', 'confirmed', 'failed', 'unknown', 'storage_error')
    ),
    receipt_status SMALLINT CHECK (receipt_status IN (0, 1)),
    initial_keeper TEXT CHECK (initial_keeper IS NULL OR initial_keeper ~ '^0x[0-9a-fA-F]{40}$'),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
