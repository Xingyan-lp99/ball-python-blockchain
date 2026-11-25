-- Internal breeder numbering is no longer part of new or existing profiles.
-- Snake identity and its on-chain associations continue to use snake_id.
ALTER TABLE snakes DROP COLUMN IF EXISTS breeder_internal_id;
