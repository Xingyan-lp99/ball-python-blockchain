-- Local demonstration accounts, each linked to an existing participant.

CREATE TABLE user_accounts (
    account_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    username TEXT NOT NULL
        CHECK (username ~ '[^[:space:]]'),

    email TEXT NOT NULL
        CHECK (email ~ '[^[:space:]]'),

    password_hash TEXT NOT NULL,

    role TEXT NOT NULL
        CHECK (role IN ('buyer', 'breeder', 'lab')),

    participant_id TEXT NOT NULL UNIQUE
        REFERENCES participants (participant_id),

    country_or_region TEXT NOT NULL
        CHECK (country_or_region ~ '[^[:space:]]'),

    contact TEXT,

    breeder_name TEXT,
    breeder_region TEXT,
    breeder_introduction TEXT,

    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT user_accounts_demo_role_binding CHECK (
        (role = 'buyer' AND participant_id = 'BUYER001')
        OR
        (role = 'breeder' AND participant_id = 'BREEDER001')
        OR
        (role = 'lab' AND participant_id IN ('LAB001', 'LAB002'))
    ),

    CONSTRAINT user_accounts_breeder_name_required CHECK (
        role <> 'breeder'
        OR (
            breeder_name IS NOT NULL
            AND breeder_name ~ '[^[:space:]]'
        )
    )
);

CREATE UNIQUE INDEX user_accounts_username_unique
    ON user_accounts (LOWER(username));

CREATE UNIQUE INDEX user_accounts_email_unique
    ON user_accounts (LOWER(email));

-- Store token hashes rather than reusable login tokens.

CREATE TABLE login_sessions (
    token_hash TEXT PRIMARY KEY,

    account_id BIGINT NOT NULL
        REFERENCES user_accounts (account_id),

    expires_at TIMESTAMPTZ NOT NULL
);
