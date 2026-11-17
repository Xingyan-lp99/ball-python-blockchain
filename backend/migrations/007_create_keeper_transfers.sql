-- Preserve transfer requests and their confirmed outcomes without changing authorship.
CREATE TABLE keeper_transfers (
    transfer_id TEXT PRIMARY KEY
        CHECK (transfer_id <> ''),

    snake_id TEXT NOT NULL
        REFERENCES snakes (snake_id),

    from_participant_id TEXT NOT NULL
        REFERENCES participants (participant_id),

    to_participant_id TEXT NOT NULL
        REFERENCES participants (participant_id),

    -- NULL means initiation has not yet been confirmed on-chain.
    status TEXT
        CHECK (status IN ('pending', 'accepted', 'rejected', 'cancelled')),

    initiated_at TIMESTAMPTZ,
    resolved_at TIMESTAMPTZ,

    CHECK (from_participant_id <> to_participant_id),

    CHECK (
        (status IS NULL AND initiated_at IS NULL AND resolved_at IS NULL)
        OR
        (
            status IS NOT NULL
            AND initiated_at IS NOT NULL
            AND (
                (status = 'pending' AND resolved_at IS NULL)
                OR
                (
                    status IN ('accepted', 'rejected', 'cancelled')
                    AND resolved_at IS NOT NULL
                    AND resolved_at >= initiated_at
                )
            )
        )
    )
);

-- Only one confirmed proposal can await recipient action for a given snake.
CREATE UNIQUE INDEX keeper_transfers_one_pending_per_snake
    ON keeper_transfers (snake_id)
    WHERE status = 'pending';

-- One transfer can link initiation and later acceptance/rejection/cancellation.
ALTER TABLE blockchain_transactions
    ADD COLUMN transfer_id TEXT
        REFERENCES keeper_transfers (transfer_id);
