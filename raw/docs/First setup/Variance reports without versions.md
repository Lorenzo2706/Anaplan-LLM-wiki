---
title: "Variance reports without versions"
source: "https://help.anaplan.com/variance-reports-without-versions-c14e86df-dc8b-47e6-8ec7-7a18bb36c367"
author:
published:
created: 2026-05-13
description: "Model builders can set up reports to compare the variance between versions in a model. Set up variance reports without versions if you don't want to increase the size of your model."
tags:
  - "clippings"
---
[Versions](https://help.anaplan.com/versions-19b4391f-5257-40ee-8dfb-36f0ab426c8f "Versions")

Model builders can set up reports to compare the variance between versions in a model. Set up variance reports without versions if you don't want to increase the size of your model.

As an alternative to versions, you can create line items to calculate variance data.

For example, you can create the line items and formulas in the table below to calculate the variance between versions. In this example, use the SELECT function to return data from Actual and Budget versions in your model.

**Note**: You can only use the SELECT function with line items.

| **Line Item** | **Formula** |
| --- | --- |
| **Actual** | Module.Line Item\[SELECT: VERSIONS.Actual\] |
| **Budget** | Module.Line Item\[SELECT: VERSIONS.Budget\] |
| **Variance** | Budget – Actual |
| **Variance %** | Variance / Actual |

You can also create line item subsets to return data from line items in different modules.

For example, you can create a line item subset with the line items and formulas in the table below. In this example, use the COLLECT function in the **Data** line item to return data from each line item in the line item subset.

| **Line Item** | **Formula** |
| --- | --- |
| **Data** | COLLECT() |
| **Actual** | Module.Line Item\[SELECT: VERSIONS.Actual\] |
| **Budget** | Module.Line Item\[SELECT: VERSIONS.Budget\] |
| **Variance** | Budget – Actual |
| **Variance %** | Variance / Actual |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fvariance-reports-without-versions-c14e86df-dc8b-47e6-8ec7-7a18bb36c367&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>