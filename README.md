# stegverse-core-lite

**Free, minimal, essential primitives for the StegVerse ecosystem.**

## What It Provides

| Module | Purpose |
|--------|---------|
| `receipt.id` | Deterministic, verifiable receipt IDs |
| `hash.deterministic` | SHA256 + seed hashing utilities |
| `interfaces.protocols` | Protocol definitions for all StegVerse components |

## Install

```bash
pip install stegverse-core-lite
```

## Quick Start

```python
from stegverse_core_lite.receipt.id import DeterministicReceiptID

provider = DeterministicReceiptID()
content = {"gate_result": "ALLOW", "confidence": 0.947}
receipt_id = provider.derive(content, seed="my-run-001")

print(receipt_id)  # 32-char deterministic ID
print(provider.verify(receipt_id, content, "my-run-001"))  # True
```

## License

MIT — free for all use, commercial or otherwise.

## Tiers

- **Lite** (this package) — Free, essential primitives
- **Full** — Governance, monitoring, notarization ([stegverse-core-full](https://github.com/GCAT-BCAT-Engine/core-full))
- **Add-ons** — LLM adapters, analytics, cross-org sync ([stegverse-core-addons](https://github.com/GCAT-BCAT-Engine/core-addons))
