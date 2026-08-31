# Vault — Index

This vault serves multiple Anaplan customers from one shared installation.
This file only routes to the index that actually catalogs pages — it is
not itself a catalog, and it never links to a model or category page
directly. Every entry below is the top of its own cascade: each
customer's index links to that customer's model/source sub-indexes, which
link to individual pages — all via Obsidian `[[wiki links]]`. This
cascade (master → customer/domain index → model/category sub-index →
page) is the core navigation structure of the vault; see CLAUDE.md §
Layers, "Cascade principle" for the full rule.

## Customers
This section grows as customers are onboarded via the `project-setup` skill —
each onboarded customer gets one `[[customers/<Name>/index]]` entry added here,
following the cascade principle above. A fresh clone starts with no entries in
this section. See `customers/registry.md` (gitignored, local-only) for the
actual current customer → model → engine list.

## Shared knowledge
- [[anaplan/index|anaplan/]] — generic Anaplan knowledge: functions, concepts, patterns, generic sources. Tracked in git, public.

## Other
- [[other-topics/index|other-topics/]] — unrelated content (e.g. Copilot Studio, GitHub Copilot notes). Gitignored.

See `customers/registry.md` for the full customer → model → engine lookup.

---

> Maintenance: touch this file only when a new customer or top-level domain is added — add one line under the right heading above, nothing more. All other index maintenance happens in the domain's own `index.md`.
