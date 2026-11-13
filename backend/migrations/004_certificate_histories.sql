CREATE TABLE certificate_histories (
    id uuid PRIMARY KEY,
    certificate_id uuid NOT NULL REFERENCES certificates(id),
    registry_kind text NOT NULL CHECK (registry_kind IN ('legacy', 'versioned')),
    chain_id bigint,
    contract_address varchar(42),
    instance_id varchar(66),
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE NULLS NOT DISTINCT (certificate_id, registry_kind, instance_id)
);
INSERT INTO certificate_histories (id, certificate_id, registry_kind, chain_id, contract_address, instance_id)
SELECT gen_random_uuid(), c.id, 'legacy', a.chain_id, a.contract_address, a.instance_id
FROM certificates c
LEFT JOIN LATERAL (
    SELECT a.chain_id, a.contract_address, a.instance_id
    FROM certificate_versions v JOIN certificate_issuance_attempts a ON a.version_id = v.id
    WHERE v.certificate_id = c.id ORDER BY a.created_at DESC, a.id DESC LIMIT 1
) a ON true;
ALTER TABLE certificate_versions ADD COLUMN history_id uuid REFERENCES certificate_histories(id);
UPDATE certificate_versions v SET history_id = h.id FROM certificate_histories h WHERE h.certificate_id = v.certificate_id;
ALTER TABLE certificate_versions ALTER COLUMN history_id SET NOT NULL;
ALTER TABLE certificate_versions DROP CONSTRAINT certificate_versions_certificate_id_version_number_key;
ALTER TABLE certificate_versions ADD CONSTRAINT uq_certificate_history_version UNIQUE (history_id, version_number);
