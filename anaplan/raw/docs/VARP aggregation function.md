---
title: "VARP aggregation function"
source: "https://help.anaplan.com/varp-aggregation-function-83078bfc-6071-4096-ac5f-5e959ac14abc"
author:
published:
created: 2026-08-31
description: "The VARP aggregation function returns the population variance of a given line item."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

This function can be useful for analyzing total employee performance rating variance by department ortotal sales revenue variance by region.

`Source[VARP: Mapping, VARP: Mapping 2, etc.]`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Source* | Number | The values to return the population variance of. |
| *Mapping* | Date, time period, list | The mapping that determines which values to return the population variance of.  This argument can be repeated to provide multiple mappings. |

The VARP aggregation function returns a numeric result.

This function is only available in the Polaris Calculation Engine.

`'Annual Performance Reviews'.'Final Score'[VARP: 'Employee Department Map'.'Department']`

- The population variance of a single value is zero.
- The population variance of a set of values, which includes NaN, is NaN.
- The square root of VARP is equal to STDEVP. See **Related Anaplan functions**, below.

- You can't use VARP with another number-typed aggregation function.
- VARP returns zero for unmapped points.
- You can't use VARP together with the **Formula** summary method.
- You can't use VARP in version formulas.

[VAR.P](https://support.microsoft.com/en-us/office/var-p-function-73d1285c-108c-4843-ba5d-a51f90656f3a)

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.25.2/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;device=desktop&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fvarp-aggregation-function-83078bfc-6071-4096-ac5f-5e959ac14abc&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>