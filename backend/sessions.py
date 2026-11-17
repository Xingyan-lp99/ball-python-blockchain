import hashlib
import secrets
from datetime import datetime, timedelta, timezone

import psycopg
from psycopg.rows import dict_row

from backend.accounts import verify_password


SESSION_LIFETIME = timedelta(hours=8)


class AuthenticationError(ValueError):
    """Credentials or the supplied session are invalid."""


def _token_hash(token: str) -> str:
    if not token or len(token) > 256:
        raise AuthenticationError("The session is invalid or expired.")

    return hashlib.sha256(token.encode("utf-8")).hexdigest()


# Purpose: authenticate credentials and create an expiring login session.
# Without this operation, account registration cannot lead to sign-in.
def create_session(
    connection: psycopg.Connection,
    *,
    username: str,
    password: str,
) -> dict[str, object]:
    with connection.transaction():
        with connection.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                """
                SELECT
                    accounts.account_id,
                    accounts.username,
                    accounts.password_hash,
                    accounts.role,
                    accounts.participant_id,
                    participants.display_name
                FROM user_accounts AS accounts
                JOIN participants
                    ON participants.participant_id = accounts.participant_id
                WHERE LOWER(accounts.username) = LOWER(%s)
                """,
                (username.strip(),),
            )
            account = cursor.fetchone()

        if account is None or not verify_password(
            password, account["password_hash"]
        ):
            raise AuthenticationError("Invalid username or password.")

        token = secrets.token_urlsafe(32)
        expires_at = datetime.now(timezone.utc) + SESSION_LIFETIME

        connection.execute(
            """
            INSERT INTO login_sessions (
                token_hash, account_id, expires_at
            )
            VALUES (%s, %s, %s)
            """,
            (_token_hash(token), account["account_id"], expires_at),
        )

    public_account = {
        key: account[key]
        for key in (
            "account_id",
            "username",
            "display_name",
            "role",
            "participant_id",
        )
    }

    return {
        "access_token": token,
        "token_type": "bearer",
        "expires_at": expires_at,
        "account": public_account,
    }


# Purpose: derive current identity from a valid, unexpired backend session.
# Without this lookup, clients could claim another role or participant.
def get_session_account(
    connection: psycopg.Connection,
    *,
    token: str,
) -> dict[str, object]:
    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(
            """
            SELECT
                accounts.account_id,
                accounts.username,
                accounts.role,
                accounts.participant_id,
                participants.display_name
            FROM login_sessions AS sessions
            JOIN user_accounts AS accounts
                ON accounts.account_id = sessions.account_id
            JOIN participants
                ON participants.participant_id = accounts.participant_id
            WHERE sessions.token_hash = %s
              AND sessions.expires_at > CURRENT_TIMESTAMP
            """,
            (_token_hash(token),),
        )
        account = cursor.fetchone()

    if account is None:
        raise AuthenticationError("The session is invalid or expired.")

    return account


# Purpose: revoke only the supplied active session on sign-out.
# Without this operation, signing out would leave the backend session usable.
def revoke_session(
    connection: psycopg.Connection,
    *,
    token: str,
) -> None:
    with connection.transaction():
        session = connection.execute(
            """
            DELETE FROM login_sessions
            WHERE token_hash = %s
              AND expires_at > CURRENT_TIMESTAMP
            RETURNING account_id
            """,
            (_token_hash(token),),
        ).fetchone()

        if session is None:
            raise AuthenticationError("The session is invalid or expired.")
