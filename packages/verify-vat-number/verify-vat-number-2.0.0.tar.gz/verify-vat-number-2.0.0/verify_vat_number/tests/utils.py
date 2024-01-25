"""Utilities for tests."""


def get_file_content(path: str) -> str:
    """Return file content as str."""
    with open(path, 'r') as handle:
        return handle.read()
