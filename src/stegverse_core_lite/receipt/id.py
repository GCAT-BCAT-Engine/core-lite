"""
Deterministic receipt ID generation.
Core primitive for accountability across StegVerse.
"""

import json
from typing import Dict, Any
from ..hash.deterministic import DeterministicHash


class DeterministicReceiptID:
    """
    Generates deterministic, verifiable receipt IDs.
    Same content + same seed = same receipt ID, always.
    """

    def __init__(self, hash_provider=None):
        self.hash_provider = hash_provider or DeterministicHash()

    def derive(self, content: Dict[str, Any], seed: str) -> str:
        """Generate deterministic receipt ID."""
        canonical = json.dumps(content, sort_keys=True, ensure_ascii=True)
        full_hash = self.hash_provider.hash(canonical, seed)
        return full_hash[:32]  # 32-char truncated ID

    def verify(self, receipt_id: str, content: Dict[str, Any], seed: str) -> bool:
        """Verify receipt ID matches content."""
        derived = self.derive(content, seed)
        return derived == receipt_id

    def derive_full(self, content: Dict[str, Any], seed: str) -> str:
        """Generate full 64-char receipt hash (for high-security contexts)."""
        canonical = json.dumps(content, sort_keys=True, ensure_ascii=True)
        return self.hash_provider.hash(canonical, seed)


def main():
    provider = DeterministicReceiptID()

    content = {
        "module": "demo-suite-runner",
        "gate_result": "ALLOW",
        "confidence": 0.947,
        "timestamp": "2026-04-26T20:07:00Z"
    }

    receipt_id = provider.derive(content, seed="publisher-run-001")
    print(f"Receipt ID: {receipt_id}")
    print(f"Verified: {provider.verify(receipt_id, content, 'publisher-run-001')}")

    # Tamper test
    bad_content = content.copy()
    bad_content["confidence"] = 0.5
    print(f"Tampered verify: {provider.verify(receipt_id, bad_content, 'publisher-run-001')}")


if __name__ == "__main__":
    main()
