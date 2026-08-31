---
title: "Planual Chapter 7 — Extensions"
type: pattern
tags: [anaplan, planual, extensions, excel, powerpoint]
created: 2026-05-04
updated: 2026-05-04
sources:
  - raw/docs/Anaplan Support 20.md
  - raw/docs/Anaplan Support 21.md
---

# Chapter 7 — Extensions

> Rules for the Microsoft Office add-ins: Excel (series 4 add-in) and PowerPoint.

Sub-sections: [Excel](#excel) · [PowerPoint](#powerpoint)

---

## Excel

The Anaplan series-4 Excel Add-in lets users access Anaplan modules and saved views from Excel.

- **Don't rename the module in Anaplan after the connection is built** — it can break the connection.
- **Use named ranges** rather than relying on cell-formula references (more robust to spreadsheet edits).
- **Upgrade to the latest version after the business has fully tested it** — don't push a fresh add-in version into live use.

## PowerPoint

The PowerPoint add-in embeds Anaplan data inside a PowerPoint deck.

- **Don't rename the module in Anaplan** — same connection-breaking risk as Excel.
- **Minimize data retrieved by the add-in.** For pulling a small slice from a large module, build a **dedicated module or view** for the add-in's use.

---

## See also

- [[wiki/patterns/planual/05-integration|Chapter 5 — Integration]] — saved-view discipline applies the same way for add-in views
