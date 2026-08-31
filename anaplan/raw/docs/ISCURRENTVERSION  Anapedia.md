---
title: "ISCURRENTVERSION | Anapedia"
source: "https://help.anaplan.com/iscurrentversion-60129c3b-faaa-46cc-b4bd-b6c692c758dd"
author:
published:
created: 2026-05-02
description: "The ISCURRENTVERSION function returns a TRUE result for the version that is set as Current in a model. It returns FALSE for all other versions."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The ISCURRENTVERSION function returns a TRUE result for the version that is set as **Current** in a model. It returns FALSE for all other versions.

For example, you can use the ISCURRENTVERSION function to ensure that a formula only applies to the Current version.

`ISCURRENTVERSION()`

The ISCURRENTVERSION function does not use any arguments.

This function returns a Boolean result.

`ISCURRENTVERSION()`

In this example, the formula returns a TRUE result for the version that is set as **Current**.

|  | **Actual** | **Budget** | **Forecast** |
| --- | --- | --- | --- |
| Current version  `ISCURRENTVERSION()` |  |  |  |

`IF ISCURRENTVERSION() THEN Sales.Year To Date Reports ELSE 0`

In this example, the formula tests if a version is the Current version. If it is, it returns the value of *Sales.Year to Date Reports*. If it is not, it returns 0.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fiscurrentversion-60129c3b-faaa-46cc-b4bd-b6c692c758dd&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>