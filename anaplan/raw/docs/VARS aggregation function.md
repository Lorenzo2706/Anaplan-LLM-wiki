---
title: "VARS aggregation function"
source: "https://help.anaplan.com/vars-aggregation-function-8af9a8dd-f765-4640-97d6-6dada4d5067f"
author:
published:
created: 2026-08-31
description: "The VARS aggregation function returns the unbiased sample variance of a given line item."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

This function can be useful for estimating sales deal variance by region or manufacturing defect rate variance.

`Source[VARS: Mapping, VARS: Mapping 2, etc.]`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Source* | Number | The values to return the sample variance of. |
| *Mapping* | Date, time period, list | The mapping that determines which values to return the sample variance of.  This argument can be repeated to provide multiple mappings. |

The VARS aggregation function returns a numeric result.

This function is only available in the Polaris Calculation Engine.

`'Recent Deals'.'Deal Value'[VARS: 'Deal Region Map'.'Sales Region']`

- The sample variance of a single value is zero.
- The sample variance of a set of values, which includes NaN, is NaN.
- The square root of VARS is equal to STDEVS. See **Related Anaplan functions**, below.

- You can't use VARS with another number-typed aggregation function.
- VARS returns zero for unmapped points.
- You can't use VARS together with the **Formula** summary method.
- You can't use VARS in version formulas.

[VAR.S](https://support.microsoft.com/en-gb/office/var-s-function-913633de-136b-449d-813e-65a00b2b990b)

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.25.2/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;device=desktop&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fvars-aggregation-function-8af9a8dd-f765-4640-97d6-6dada4d5067f&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>