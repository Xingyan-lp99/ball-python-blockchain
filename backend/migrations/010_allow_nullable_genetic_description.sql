-- Allow missing genetic descriptions while preserving historical values and CHECK.
-- Reapplying this migration leaves the same nullable column definition.
BEGIN;

SET LOCAL lock_timeout = '5s';

ALTER TABLE public.snakes
    ALTER COLUMN genetic_description DROP NOT NULL;

COMMIT;
