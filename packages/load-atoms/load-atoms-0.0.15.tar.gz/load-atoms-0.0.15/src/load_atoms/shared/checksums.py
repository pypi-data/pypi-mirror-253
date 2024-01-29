from __future__ import annotations

import hashlib
import string
from pathlib import Path


def generate_checksum(file_path: Path | str) -> str:
    """Generate a checksum for a file."""

    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    return sha256_hash.hexdigest()[:12]


def valid_checksum(hash: str) -> bool:
    """Check if a hash is valid."""
    if len(hash) != 12:
        return False
    return all(c in string.hexdigits for c in hash)


def matches_checksum(file_path: Path, hash: str) -> bool:
    """Check if a file matches a given hash."""
    return generate_checksum(file_path) == hash
