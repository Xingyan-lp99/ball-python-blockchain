-- One current wallet challenge per login session; never store the bearer token.
-- Sign-out removes the session and its challenge through the foreign key.
CREATE TABLE wallet_challenges (
    session_token_hash TEXT PRIMARY KEY
        REFERENCES login_sessions (token_hash) ON DELETE CASCADE,
    nonce TEXT NOT NULL UNIQUE CHECK (nonce ~ '^[0-9a-f]{32}$'),
    wallet_address TEXT NOT NULL
        CHECK (wallet_address ~ '^0x[0-9a-fA-F]{40}$'),
    message TEXT NOT NULL CHECK (message <> ''),
    issued_at TIMESTAMPTZ NOT NULL,
    expires_at TIMESTAMPTZ NOT NULL,
    used_at TIMESTAMPTZ,
    CHECK (expires_at > issued_at),
    CHECK (used_at IS NULL OR (used_at >= issued_at AND used_at < expires_at))
);
