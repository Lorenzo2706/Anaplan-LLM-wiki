---
name: first-setup
description: >
  Bootstrap a freshly cloned copy of this Anaplan LLM wiki template into a working vault.
  Trigger whenever the user says "run first-time setup", "set up this vault", "bootstrap
  this repo", "initial setup", "onboard this repo", "flatten the sample docs", or any
  similar phrasing — or whenever you notice `CLAUDE.md.example` exists but `CLAUDE.md`
  does not yet, which signals an unbootstrapped clone. Handles: flattening the shipped
  `raw/docs/First setup/` sample bundle, simplifying `.gitignore`, adopting `CLAUDE.md`
  from the example (with the transitional callouts stripped), and verifying which skills
  are present vs. still need installing from the Cowork skill store. One-time per vault —
  always check current state first so re-running is a safe no-op.
---

# First Setup — Bootstrap a Fresh Vault

This skill turns a freshly cloned copy of this repo into a working vault, per the Setup
section of `README.md`. It is idempotent — always inspect current state before acting so
re-running against an already-set-up vault does nothing destructive.

---

## Phase 0 — Detect current state

Before changing anything, check:

1. Does `raw/docs/First setup/` exist?
2. Does `CLAUDE.md` already exist at the vault root (as opposed to only `CLAUDE.md.example`)?
3. Does `.gitignore` still contain the `First setup`-specific carve-out (`/raw/docs/*` /
   `!/raw/docs/First setup`)?
4. Which skill folders exist under `.claude/skills/`?

If **both** (1) is false and (2) is true, the vault is already set up — tell the user so
and ask whether they want you to re-verify anyway rather than silently doing nothing.

---

## Phase 1 — Flatten the sample docs

Only if `raw/docs/First setup/` exists:

1. List its contents and list the contents of `raw/docs/` directly. If any filename
   collides between the two, stop and ask the user how to resolve it (overwrite, rename,
   or skip) — never silently overwrite.
2. Move every file from `raw/docs/First setup/` up into `raw/docs/`.
3. Delete the now-empty `raw/docs/First setup/` folder.
4. If `.gitignore` has the `First setup`-specific carve-out (see Phase 0, check 3),
   simplify it back to the standard convention:
   ```diff
    /raw/*
    !/raw/docs
   -/raw/docs/*
   -!/raw/docs/First setup
   ```
   Skip this edit if the repo isn't under version control, or if the user has already
   customized `.gitignore` beyond this pattern (ask first in that case).

Use whatever move/delete mechanism fits the current OS (`Move-Item`/`Remove-Item` on
Windows PowerShell, `mv`/`rm` on POSIX shells) — the repo's own README examples use
PowerShell, but don't assume that shell is available.

---

## Phase 2 — Adopt `CLAUDE.md`

Only if `CLAUDE.md` does not already exist:

1. Copy `CLAUDE.md.example` to `CLAUDE.md` (keep the `.example` file in place — it's the
   template's reference copy for future upstream updates).
2. In the new `CLAUDE.md`, strip the transitional callouts that only make sense on the
   shipped (unflattened) layout — they no longer apply once Phase 1 has run:
   - The `> [!note] This reference repo ships its sample docs nested under raw/docs/First
     setup/ ...` callout under **Version control**.
   - The trailing sentence on the `wiki-data-ingestion` skill bullet starting "If you're
     still on the shipped sample layout, exclude `raw/docs/First setup/` ...".

   If Phase 1 was skipped (e.g. the user already flattened manually, or declined), leave
   these notes in place — they're still accurate.
3. Ask the user for the values needed to personalize `CLAUDE.md`:
   - Vault root path, to replace `<your-vault-root>` (default to the current working
     directory if the user has no preference).
   - Model names and engines, to replace the `ModelA`/`ModelB` placeholders in the
     **Engine defaults** bullet under "Anaplan-specific guidance" — ask directly: "Which
     Anaplan models will this vault track, and is each one Classic or Polaris?" If they
     don't know yet, leave the placeholder and note it as a follow-up.
   - Any team-specific naming conventions worth capturing now (optional — don't press if
     the user has none yet).

---

## Phase 3 — Verify skills

1. Report which of `anaplan-formula-agent` and `anaplan-module-mapping` are present under
   `.claude/skills/` (they ship with the repo, so normally both are).
2. Check whether `wiki-lint` and `wiki-data-ingestion` are available (as project-skill
   folders under `.claude/skills/`, or otherwise accessible via the `Skill` tool). These
   ship as Cowork plugin skills, not repo files — if they're missing, tell the user to
   install them from the Cowork skill store and that ingest/lint won't work until they do.

---

## Phase 4 — Summary

End with a structured summary, always — even if some phases were skipped because the
vault was already partially set up:

```
## First setup complete

**Flattened:** [raw/docs/First setup/ → raw/docs/, N files moved | already flat | skipped: <reason>]
**.gitignore:** [simplified | left as-is: <reason>]
**CLAUDE.md:** [created from example, transitional notes stripped | already existed | pending values: <list>]
**Skills present:** anaplan-formula-agent [✓/✗], anaplan-module-mapping [✓/✗], wiki-lint [✓/✗], wiki-data-ingestion [✓/✗]

**Follow-ups for the user:**
- [e.g. "fill in engine defaults once models are known", "install wiki-lint/wiki-data-ingestion from the Cowork skill store"]
```

If nothing is outstanding, say so explicitly: "Vault is fully set up — ready for your
first ingest."
