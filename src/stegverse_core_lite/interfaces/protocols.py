"""
Protocol definitions for stegverse-core-lite.
All interface contracts used across the StegVerse ecosystem.
"""

from typing import Protocol, Dict, Any, runtime_checkable


@runtime_checkable
class HashProvider(Protocol):
    """Deterministic hashing with seed support."""

    def hash(self, content: str, seed: str = "") -> str: ...
    def verify(self, content: str, seed: str, expected_hash: str) -> bool: ...


@runtime_checkable
class ReceiptIDProvider(Protocol):
    """Deterministic receipt ID generation and verification."""

    def derive(self, content: Dict[str, Any], seed: str) -> str: ...
    def verify(self, receipt_id: str, content: Dict[str, Any], seed: str) -> bool: ...


@runtime_checkable
class StegVerseProtocol(Protocol):
    """Base protocol for all StegVerse components."""

    def version(self) -> str: ...
    def health_check(self) -> Dict[str, Any]: ...
