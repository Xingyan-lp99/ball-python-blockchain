import os

import psycopg

from backend.blockchain import check_blockchain_connection


# Purpose: associate demo participants with distinct local Hardhat accounts.
# Workflow: demo setup before registration, reports, and keeper transfer.
# Without these records, the backend cannot identify the acting participant.
def seed_demo_participants(*, password: str) -> list[tuple[str, str]]:
    chain = check_blockchain_connection(
        rpc_url="http://127.0.0.1:8545",
        expected_chain_id=31337,
    )
    accounts = chain["accounts"]

    if not isinstance(accounts, list) or len(accounts) < 5:
        raise RuntimeError("At least five local accounts are required.")

    participants = [
        ("BREEDER001", "Demo Breeder", accounts[1]),
        ("LAB001", "Demo Laboratory 1", accounts[2]),
        ("LAB002", "Demo Laboratory 2", accounts[3]),
        ("BUYER001", "Demo Buyer", accounts[4]),
    ]

    with psycopg.connect(
        host="127.0.0.1",
        port=5433,
        dbname="ballpython_demo",
        user="ballpython",
        password=password,
        connect_timeout=5,
    ) as connection:
        for participant_id, display_name, wallet_address in participants:
            connection.execute(
                """
                INSERT INTO public.participants (
                    participant_id, display_name, wallet_address
                )
                VALUES (%s, %s, %s)
                ON CONFLICT DO NOTHING
                """,
                (participant_id, display_name, wallet_address),
            )

            stored = connection.execute(
                """
                SELECT wallet_address
                FROM public.participants
                WHERE participant_id = %s
                """,
                (participant_id,),
            ).fetchone()

            if stored is None or stored[0].lower() != wallet_address.lower():
                raise RuntimeError(
                    f"Participant mapping conflicts for {participant_id}. "
                    "No changes were committed."
                )

    return [
        (participant_id, wallet_address)
        for participant_id, _, wallet_address in participants
    ]


if __name__ == "__main__":
    password = os.environ.get("DEMO_DB_PASSWORD")

    if not password:
        raise RuntimeError("DEMO_DB_PASSWORD is not set.")

    mappings = seed_demo_participants(password=password)

    print("Demo participants initialized successfully.")
    for participant_id, wallet_address in mappings:
        print(f"{participant_id}: {wallet_address}")