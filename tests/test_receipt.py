"""Tests for deterministic receipt ID generation."""

import pytest
from stegverse_core_lite.receipt.id import DeterministicReceiptID


class TestDeterministicReceiptID:
    def test_determinism(self):
        provider = DeterministicReceiptID()
        content = {"test": "data", "value": 42}
        seed = "test-seed"

        id1 = provider.derive(content, seed)
        id2 = provider.derive(content, seed)

        assert id1 == id2
        assert len(id1) == 32

    def test_verify_success(self):
        provider = DeterministicReceiptID()
        content = {"gate": "ALLOW", "confidence": 0.95}
        seed = "verify-test"

        rid = provider.derive(content, seed)
        assert provider.verify(rid, content, seed) is True

    def test_verify_failure(self):
        provider = DeterministicReceiptID()
        content = {"gate": "ALLOW", "confidence": 0.95}
        seed = "verify-test"

        rid = provider.derive(content, seed)
        bad_content = {"gate": "DENY", "confidence": 0.95}

        assert provider.verify(rid, bad_content, seed) is False

    def test_different_seeds_different_ids(self):
        provider = DeterministicReceiptID()
        content = {"same": "content"}

        id1 = provider.derive(content, "seed-a")
        id2 = provider.derive(content, "seed-b")

        assert id1 != id2
