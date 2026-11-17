from typing import Annotated

from fastapi import Depends, HTTPException

from backend.session_routes import CurrentAccountResponse, read_current_account


# Resolve identity from the backend session for every protected request.
AuthenticatedAccount = Annotated[
    CurrentAccountResponse, Depends(read_current_account)
]


# Purpose: reserve initial profile registration for the signed-in breeder.
# Without this check, another account role could use the registration endpoint.
def require_breeder(account: AuthenticatedAccount) -> CurrentAccountResponse:
    if account.role != "breeder":
        raise HTTPException(
            status_code=403,
            detail="Only a breeder account may register a snake.",
        )
    return account


# Purpose: admit care-record roles before the live keeper and author checks.
# Without this dependency, a laboratory role could enter the husbandry write flow.
def require_husbandry_role(
    account: AuthenticatedAccount,
) -> CurrentAccountResponse:
    if account.role not in {"buyer", "breeder"}:
        raise HTTPException(
            status_code=403,
            detail="Only buyer or breeder accounts may maintain husbandry records.",
        )
    return account


BreederAccount = Annotated[CurrentAccountResponse, Depends(require_breeder)]
HusbandryAccount = Annotated[
    CurrentAccountResponse, Depends(require_husbandry_role)
]


# Purpose: restrict certificate issuance to signed-in laboratory staff.
# Without this check, another account role could enter the issuance workflow.
def require_laboratory(
    account: AuthenticatedAccount,
) -> CurrentAccountResponse:
    if account.role != "lab":
        raise HTTPException(
            status_code=403,
            detail="Only laboratory accounts may issue certificates.",
        )
    return account


LaboratoryAccount = Annotated[
    CurrentAccountResponse,
    Depends(require_laboratory),
]


# Purpose: admit keeper roles before checking the snake's live on-chain authority.
# Without this dependency, laboratory accounts could enter the transfer write flow.
def require_keeper_role(account: AuthenticatedAccount) -> CurrentAccountResponse:
    if account.role not in {"buyer", "breeder"}:
        raise HTTPException(
            status_code=403,
            detail="Only buyer or breeder accounts may request keeper transfers.",
        )
    return account


KeeperAccount = Annotated[CurrentAccountResponse, Depends(require_keeper_role)]
