# Line Items in Anaplan (demo source)

> This is a synthetic placeholder source used to demonstrate the ingestion workflow. Replace with real Anapedia clippings, PDFs, or CSVs.

A **line item** is the basic building block of a module. Each line item holds values across the dimensions of the module it belongs to. Line items have a *Format* (Number, Boolean, Date, Time Period, List, Text), a *Formula* (optional), and a *Summary* method (Sum, Average, Min, Max, None, Formula, Ratio).

Line items can be classified by purpose:
- **Input** — entered by users or imported from data.
- **Calculation** — derived via a formula from other line items.
- **Output** — consumed by dashboards or downstream modules.

Best practice (DISCO methodology) is to split modules so that line items in a single module share a purpose: Data hubs, Inputs, System, Calculations, or Outputs.

Common formats: Number (most calculations), Boolean (flags), List (mappings), Time Period (date math).
