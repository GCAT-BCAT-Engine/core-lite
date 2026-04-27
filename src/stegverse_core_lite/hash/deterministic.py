"""
Deterministic SHA256 hashing with seed support.
Core primitive for all StegVerse verification.
"""

import hashlib
from typing import Dict, Any


class DeterministicHash:
    """
    SHA256-based deterministic hashing.
    Same content + same seed = same hash, always.
    """

    ALGORITHM = "sha256"

    @classmethod
    def hash(cls, content: str, seed: str = "") -> str:
        """Generate deterministic hash from content and seed."""
        composite = f"{content}::{seed}"
        return hashlib.sha256(composite.encode("utf-8")).hexdigest()

    @classmethod
    def hash_dict(cls, content: Dict[str, Any], seed: str = "") -> str:
        """Hash a dictionary by canonicalizing it first."""
        import json
        canonical = json.dumps(content, sort_keys=True, ensure_ascii=True)
        return cls.hash(canonical, seed)

    @classmethod
    def verify(cls, content: str, seed: str, expected_hash: str) -> bool:
        """Verify content matches expected hash."""
        return cls.hash(content, seed) == expected_hash

    @classmethod
    def verify_dict(cls, content: Dict[str, Any], seed: str, expected_hash: str) -> bool:
        """Verify dictionary matches expected hash."""
        return cls.hash_dict(content, seed) == expected_hash


def main():
    # Demo
    h = DeterministicHash.hash("test content", seed="demo-seed-001")
    print(f"Hash: {h}")
    print(f"Verify: {DeterministicHash.verify('test content', 'demo-seed-001', h)}")

    data = {"gate_result": "ALLOW", "confidence": 0.947}
    h2 = DeterministicHash.hash_dict(data, seed="run-001")
    print(f"Dict hash: {h2}")
    print(f"Dict verify: {DeterministicHash.verify_dict(data, 'run-001', h2)}")


if __name__ == "__main__":
    main()
