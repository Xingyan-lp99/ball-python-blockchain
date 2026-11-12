"""Temporary server-side demo identity. This is NOT authentication."""


def get_current_breeder_id() -> str:
    return "BR001"


def get_current_lab_id() -> str:
    """Server demo endpoint identity, NOT an authenticated user/role selector."""
    return "LAB001"
