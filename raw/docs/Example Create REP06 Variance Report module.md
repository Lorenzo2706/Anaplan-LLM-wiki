---
title: "Example: Create REP06 Variance Report module"
source: "https://help.anaplan.com/example-create-rep06-variance-report-module-30b4a210-8ac9-4832-bd01-97381f8c996d"
author:
published:
created: 2026-05-13
description: "As part of the line item subset example, create a variance report module called REP06 Variance Report. You add this module to a card on a UX page so you can see the variance per country."
tags:
  - "clippings"
---
As part of the line item subset example, create a variance report module called *REP06 Variance Report*. You add this module to a card on a UX page so you can see the variance per country.

**Note**: See [Line item subset example](https://help.anaplan.com/84d95131-a83a-45b7-ba41-71defbb732ff) for the complete list of steps.

In the module, put the line item subset *LIS: Multi-variance report* on **Rows,** line items on **Columns**, andthe *G2 Country* list, and the *Users* list on **Pages**. The Time dimension does not apply to this module because we want to see the difference between months.

Add the following line items:

|  | **Format** | **Formula** | **Applies To** |
| --- | --- | --- | --- |
| **REP06 Variance Report** |  |  | G2 Country, Users, LIS: Multi-variance reporting |
| Month 1 | Number | `'REP05 Variance Report Staging'.Data[LOOKUP: 'SYS11 Time Variance Reporting'.'Month 1']` |  |
| Month 2 | Number | `'REP05 Variance Report Staging'.Data[LOOKUP: 'SYS11 Time Variance Reporting'.'Month 2']` |  |
| Variance | Number | `'Month 2' - 'Month 1'` |  |
| % Variance | Number:   Percentage | `Variance / 'Month 1'` |  |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fexample-create-rep06-variance-report-module-30b4a210-8ac9-4832-bd01-97381f8c996d&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>