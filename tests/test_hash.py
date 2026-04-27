"""Tests for deterministic hashing."""

import pytest
from stegverse_core_lite.hash.deterministic import DeterministicHash


class TestDeterministicHash:
    def test_hash_determinism(self):
        h1 = DeterministicHash.hash("content", "seed")
        h2 = DeterministicHash.hash("content", "seed")
        assert h1 == h2
        assert len(h1) == 64  # Full SHA256

    def test_verify(self):
        h = DeterministicHash.hash("content", "seed")
        assert DeterministicHash.verify("content", "seed", h) is True
        assert DeterministicHash.verify("wrong", "seed", h) is False

    def test_dict_hash(self):
        data = {"a": 1, "b": 2}
        h1 = DeterministicHash.hash_dict(data, "seed")
        h2 = DeterministicHash.hash_dict({"b": 2, "a": 1}, "seed")  # Different order
        assert h1 == h2  # Canonicalization ensures same hash
