---
title: "Changes to the Fiscal Year Label"
source: "https://help.anaplan.com/changes-to-the-fiscal-year-label-b5fd95e3-86ec-4e4c-8807-3463d3fe0747"
author:
published:
created: 2026-05-13
description: "The Fiscal Year Label appears in modules that use the Time dimension. The default label is FY. If you change the Fiscal Year Label to CY, to represent calendar years, it might impact imports."
tags:
  - "clippings"
---
The **Fiscal Year Label** appears in modules that use the Time dimension. The default label is **FY**. If you change the **Fiscal Year Label** to **CY**, to represent calendar years, it might impact imports.

If you import data into a module that uses **Months** in the **Time Scale** column, there's no impact when you change the **Fiscal Year Label**.

If you import data into a module that uses one of the following time scales, you may need to reconfigure your imports when you change the **Fiscal Year Label**:

- **Weeks**
- **Periods** (if you have **13 4-week Periods** as the **Calendar Type**)
- **Quarters**
- **Half Year**
- **Year**

For example, take a module that uses one of the above time scales and run an import set to match on **Name only**. In this case, the import is unsuccessful, and you will see the message **Invalid date or timescale identifier**.

To fix imports, use the [**Custom fixed-position pattern**](https://help.anaplan.com/anapedia/Content/Import_and_Export/Import_Data_into_Models/Map_the_Timescale.html) import option when you map the Time dimension. Alternatively, change the time label in the source data.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fchanges-to-the-fiscal-year-label-b5fd95e3-86ec-4e4c-8807-3463d3fe0747&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>