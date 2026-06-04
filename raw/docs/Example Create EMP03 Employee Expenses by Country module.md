---
title: "Example: Create EMP03 Employee Expenses by Country module"
source: "https://help.anaplan.com/example-create-emp03-employee-expenses-by-country-module-d52da97f-02ab-4dba-acc8-87f336c4035f"
author:
published:
created: 2026-05-13
description: "Create the EMP03 Employee Expenses by Country module. Use this module as part of the line item subset example."
tags:
  - "clippings"
---
Create the *EMP03 Employee Expenses by Country* module. Use this module as part of the line item subset example.

**Note**: See [Line item subset example](https://help.anaplan.com/84d95131-a83a-45b7-ba41-71defbb732ff) for the complete list of steps.

The module contains the *G2 Country* list on **Pages** and Time on **Columns**. The line items are on **Rows** as shown in the table:

|  | **Format** | **Formula** |
| --- | --- | --- |
| **EMP03 Employee Expenses by Country** | Number |  |
| Headcount | Number | `'EMP02 Employee Expenses'.Headcount[SUM: 'SYS08 Employee Details'.Country]` |
| Salary | Number | `'EMP02 Employee Expenses'.Salary[SUM: 'SYS08 Employee Details'.Country]` |
| Bonus | Number | `'EMP02 Employee Expenses'.Bonus[SUM: 'SYS08 Employee Details'.Country]` |
| Car costs | Number | `'EMP02 Employee Expenses'.Car Costs[SUM: 'SYS08 Employee Details'.Country]` |
| Phone costs | Number | `'EMP02 Employee Expenses'.Phone Costs[SUM: 'SYS08 Employee Details'.Country]` |
| Medical costs | Number | `'EMP02 Employee Expenses'.Medical Costs[SUM: 'SYS08 Employee Details'.Country]` |
| **Total employee expenses** | Number | `Salary + Bonus + Car costs + Phone costs + Medical costs` |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fexample-create-emp03-employee-expenses-by-country-module-d52da97f-02ab-4dba-acc8-87f336c4035f&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>