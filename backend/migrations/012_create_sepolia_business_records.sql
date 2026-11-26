-- Keep Sepolia certificate and transfer records separate from Anvil business tables.
ALTER TABLE public.sepolia_pet_registrations
    ADD COLUMN IF NOT EXISTS current_keeper TEXT
        CHECK (current_keeper IS NULL OR current_keeper ~ '^0x[0-9a-fA-F]{40}$');

UPDATE public.sepolia_pet_registrations
SET current_keeper = initial_keeper
WHERE current_keeper IS NULL AND initial_keeper IS NOT NULL;

CREATE TABLE IF NOT EXISTS public.sepolia_business_transactions (
    transaction_id BIGSERIAL PRIMARY KEY,
    operation TEXT NOT NULL,
    business_id TEXT NOT NULL,
    snake_id TEXT NOT NULL REFERENCES public.sepolia_pet_registrations (snake_id),
    signer_participant_id TEXT NOT NULL REFERENCES public.participants (participant_id),
    contract_address TEXT NOT NULL CHECK (contract_address ~ '^0x[0-9a-fA-F]{40}$'),
    transaction_hash TEXT NOT NULL UNIQUE CHECK (transaction_hash ~ '^0x[0-9a-fA-F]{64}$'),
    transaction_nonce BIGINT NOT NULL CHECK (transaction_nonce >= 0),
    transaction_status TEXT NOT NULL CHECK (
        transaction_status IN ('prepared', 'submitted', 'confirmed', 'failed', 'unknown')
    ),
    receipt_status SMALLINT CHECK (receipt_status IN (0, 1)),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (operation, business_id)
);

CREATE TABLE IF NOT EXISTS public.sepolia_certificate_series (
    series_id TEXT PRIMARY KEY CHECK (series_id <> ''),
    snake_id TEXT NOT NULL REFERENCES public.sepolia_pet_registrations (snake_id),
    laboratory_id TEXT NOT NULL REFERENCES public.laboratories (laboratory_id),
    title TEXT NOT NULL CHECK (title ~ '[^[:space:]]'),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.sepolia_certificate_versions (
    version_id TEXT PRIMARY KEY CHECK (version_id <> ''),
    series_id TEXT NOT NULL REFERENCES public.sepolia_certificate_series (series_id),
    version_number INTEGER NOT NULL CHECK (version_number > 0),
    previous_version_id TEXT REFERENCES public.sepolia_certificate_versions (version_id),
    file_reference TEXT NOT NULL CHECK (file_reference ~ '[^[:space:]]'),
    file_hash TEXT NOT NULL CHECK (file_hash ~ '^[0-9a-f]{64}$'),
    issuer_address TEXT NOT NULL CHECK (issuer_address ~ '^0x[0-9a-fA-F]{40}$'),
    status SMALLINT CHECK (status IN (1, 2)),
    issued_at TIMESTAMPTZ,
    transaction_id BIGINT NOT NULL UNIQUE REFERENCES public.sepolia_business_transactions (transaction_id),
    UNIQUE (series_id, version_number),
    CHECK (
        (version_number = 1 AND previous_version_id IS NULL)
        OR (version_number > 1 AND previous_version_id IS NOT NULL)
    )
);

CREATE UNIQUE INDEX IF NOT EXISTS sepolia_certificate_one_unconfirmed_version
    ON public.sepolia_certificate_versions (series_id)
    WHERE status IS NULL;

CREATE TABLE IF NOT EXISTS public.sepolia_keeper_transfers (
    transfer_id TEXT PRIMARY KEY CHECK (transfer_id <> ''),
    snake_id TEXT NOT NULL REFERENCES public.sepolia_pet_registrations (snake_id),
    from_participant_id TEXT NOT NULL REFERENCES public.participants (participant_id),
    to_participant_id TEXT NOT NULL REFERENCES public.participants (participant_id),
    from_address TEXT NOT NULL CHECK (from_address ~ '^0x[0-9a-fA-F]{40}$'),
    to_address TEXT NOT NULL CHECK (to_address ~ '^0x[0-9a-fA-F]{40}$'),
    status TEXT NOT NULL CHECK (status IN ('prepared', 'pending', 'accepted', 'failed', 'unknown')),
    initiated_at TIMESTAMPTZ,
    resolved_at TIMESTAMPTZ,
    initiation_transaction_id BIGINT NOT NULL UNIQUE REFERENCES public.sepolia_business_transactions (transaction_id),
    acceptance_transaction_id BIGINT UNIQUE REFERENCES public.sepolia_business_transactions (transaction_id),
    CHECK (from_participant_id <> to_participant_id),
    CHECK (LOWER(from_address) <> LOWER(to_address))
);

CREATE UNIQUE INDEX IF NOT EXISTS sepolia_keeper_transfers_one_open_per_pet
    ON public.sepolia_keeper_transfers (snake_id)
    WHERE status IN ('prepared', 'pending', 'unknown');
