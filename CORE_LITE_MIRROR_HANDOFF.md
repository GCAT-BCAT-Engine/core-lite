# GCAT-BCAT Core-Lite Mirror Handoff

## Status

This file is the active handoff and task source of truth for `GCAT-BCAT-Engine/core-lite` until superseded.

## Current goal

Repair Architecture Guard failure by installing an explicit `stegverse.architecture.json` manifest for the current telemetry schema surface.

## Installed repair artifacts

```text
stegverse.architecture.json
config/stegdb-schema.yml
```

## Boundary

The architecture manifest is an inventory and validation boundary. It does not grant runtime authority, execution authority, or cross-repo mutation authority.

## Remaining files or modules to install

```text
Future hardening candidate -> GCAT-BCAT-Engine/core-lite: stricter architecture manifest once repo structure expands beyond config/stegdb-schema.yml.
Future propagation candidate -> StegVerse-Labs/Site: Repo Operations Center status surface.
Future propagation candidate -> GCAT-BCAT-Engine/Publisher: architecture repair status artifact.
Future propagation candidate -> admissibility-wiki: architecture guard admissibility note.
Future propagation candidate -> stegguardian-wiki: operator-facing architecture guard boundary note.
```

## Verification

Expected guard path:

```bash
.github/workflows/architecture-guard.yml
```

The current repair keeps enforcement at `warn` until a fuller structure is declared.

## Archive posture

This handoff records the current repair path so the complete thread can be archived without additional context.
