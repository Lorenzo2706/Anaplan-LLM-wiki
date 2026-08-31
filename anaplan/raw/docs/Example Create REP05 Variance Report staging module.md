---
title: "Example: Create REP05 Variance Report staging module"
source: "https://help.anaplan.com/example-create-rep05-variance-report-staging-module-37dfbb55-5a5b-4277-8ffe-0d9dd419efa4"
author:
published:
created: 2026-05-13
description: "As part of the line item subset example, create a staging module. This module uses the COLLECT() function to pull the data from a line item subset."
tags:
  - "clippings"
---
As part of the line item subset example, create a staging module. This module uses the COLLECT() function to pull the data from a line item subset.

**Note**: See [Line item subset example](https://help.anaplan.com/84d95131-a83a-45b7-ba41-71defbb732ff) for the complete list of steps.

Name the module *REP05 Variance Report Staging.* Put the *G2 Country* list and line items on **Pages**, the **Time** dimension on columns, and the subset *LIS: Multi-variance reporting* on **Rows**.

Add a line item called *Data* and format *Data* as shown:

|  | **Format** | **Formula** | **Summary** | **Applies To** | **Time Scale** |
| --- | --- | --- | --- | --- | --- |
| **REP05 Variance Report Staging** |  |  |  | G2 Country, LIS: Multi-variance reporting | Month |
| Data | Number | COLLECT() | NONE | \- | Month |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fexample-create-rep05-variance-report-staging-module-37dfbb55-5a5b-4277-8ffe-0d9dd419efa4&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>