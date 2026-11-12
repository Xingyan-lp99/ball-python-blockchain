CREATE TABLE snakes (
    id uuid PRIMARY KEY,
    snake_id text NOT NULL,
    name text,
    sex text NOT NULL,
    date_of_birth date,
    breeder_internal_id text,
    morph_description text,
    breeder_id text NOT NULL,
    current_manager_id text NOT NULL,
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_snakes_snake_id UNIQUE (snake_id),
    CONSTRAINT ck_snakes_snake_id CHECK (length(btrim(snake_id)) > 0 AND snake_id = btrim(snake_id)),
    CONSTRAINT ck_snakes_sex CHECK (sex IN ('male', 'female', 'unknown')),
    CONSTRAINT ck_snakes_date_of_birth CHECK (date_of_birth <= (CURRENT_TIMESTAMP AT TIME ZONE 'UTC')::date)
);
