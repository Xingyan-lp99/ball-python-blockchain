-- Require a nonblank sex description for each snake profile.

ALTER TABLE snakes
    ALTER COLUMN sex SET NOT NULL,
    ADD CONSTRAINT snakes_sex_not_blank
        CHECK (sex ~ '[^[:space:]]');