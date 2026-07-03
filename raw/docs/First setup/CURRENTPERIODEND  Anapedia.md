---
title: "CURRENTPERIODEND | Anapedia"
source: "https://help.anaplan.com/currentperiodend-5c7aa5ad-1a45-4b48-8dca-6707ba964883"
author:
published:
created: 2026-05-02
description: "The CURRENTPERIODEND function returns the end date from a model's current period."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, you can use the CURRENTPERIODEND function to ensure that a formula only applies to a specific week in the current period.

`CURRENTPERIODEND()`

The CURRENTPERIODEND function does not use any arguments.

This function returns a date result.

`CURRENTPERIODEND()`

In this example, the formula returns the end date from the current period.

You can set your model's **Current Period** in **Time** in the model settings bar.

`PERIOD(CURRENTPERIODEND() + 1)`

In this example, the formula returns the first time period after the model's current period. If the model's current period is *Jan 20*, it returns *Feb 20*.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fcurrentperiodend-5c7aa5ad-1a45-4b48-8dca-6707ba964883&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>