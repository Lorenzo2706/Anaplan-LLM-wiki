---
title: "Variance reports with versions"
source: "https://help.anaplan.com/variance-reports-with-versions-bd3ad610-2ea4-4bb2-aa87-d0fb0b73a475"
author:
published:
created: 2026-05-13
description: "Model builders can set up reports to compare the variance between versions in a model."
tags:
  - "clippings"
---
[Versions](https://help.anaplan.com/versions-19b4391f-5257-40ee-8dfb-36f0ab426c8f "Versions")

For example, you can view actual and budget data for a model’s **Current Period**.

**Note**: If you change the **Current Period** in your model, variance reports update automatically. Configure the **Current Period** in **Time** in the model settings bar.

You can create **Variance** and **Variance %** versions in **Versions** in the model settings bar. Add formulas in the **Formula** column to compare figures for a time period. Learn more in [Create versions](https://help.anaplan.com/78fa342e-9c6d-4dff-95e4-e34d725e6eb7).

In this example, the formulas calculate the variance between Actual and Budget versions.

|  | **Current** | **Actual** | **Switchover** | **Formula** |
| --- | --- | --- | --- | --- |
| **Actual** |  |  |  |  |
| **Budget** |  |  | Jan 20 |  |
| **Variance** |  |  |  | Actual - Budget |
| **Variance %** |  |  |  | `IF Budget > 0 THEN 100 * (Actual – Budget) / Budget ELSE 100 * (Budget – Actual) / Budget` |

In this module example, the formulas calculate the variance between actual and budget data for the **Revenue** and **Cost of Goods** line items.

|  | **Actual** | **Budget** | **Variance** | **Variance %** |
| --- | --- | --- | --- | --- |
| **Revenue** | 25,452,858 | 25,483,000 | \-30,142 | \-0.1183 |
| **Cost of Goods** | \-13,980,684 | \-14,600,000 | 619,316 | 4.242 |
| **Formula** |  |  | Actual - Budget | `IF Budget > 0 THEN 100 * (Actual – Budget) / Budget ELSE 100 * (Budget – Actual) / Budget` |

Learn more in [Add version formulas to a model](https://help.anaplan.com/c2f94eb6-3c04-465d-8b82-7926bdf1be42).

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fvariance-reports-with-versions-bd3ad610-2ea4-4bb2-aa87-d0fb0b73a475&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>