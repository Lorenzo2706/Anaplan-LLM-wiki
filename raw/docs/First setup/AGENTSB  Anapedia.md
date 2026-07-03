---
title: "AGENTSB | Anapedia"
source: "https://help.anaplan.com/agentsb-231ff255-172a-4586-a7de-0318c8bbea4d"
author:
published:
created: 2026-05-02
description: "The AGENTSB function calculates the number of servers required to answer a specified percentage of calls (or SLA) within a busy period."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The AGENTSB function calculates the number of servers required to answer a specified percentage of calls (or SLA) within a busy period.

You can use the AGENTSB function with other functions such as AGENTS, ERLANGB, and ERLANGC to account for a range of resource management situations.

`AGENTSB(SLA, Arrival rate, Average duration)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *SLA* | Number | The percentage of requests that need to be processed within the *Target response time*. |
| *Arrival rate* | Number | The interval between the arrival of each request. |
| *Average duration* | Number | The average duration it takes to process each request. |

The AGENTSB function returns a number, which is the number of agents required to prevent any requests being placed on hold.

Call center planning functions are unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

The *Arrival rate* and *Average duration* arguments do not have to use a specific time unit. For example, they can be seconds or minutes. However, both arguments must use the same time unit.

In this example, the *Call Centers* list is on columns, and line items on rows. The three line items contain the data for the AGENTSB function for each call center:

- The percentage of calls that must be responded to within the target response time, or SLA (uses the [percentage number **Format**](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a))
- The interval between each request arriving
- The average duration it takes to complete requests

The *Servers to meet SLA* line item uses the AGENTS function to calculate how many agents are needed to answer the percentage of calls specified in the SLA.

|  | **Call Center 1** | **Call Center 2** | **Call Center 3** | **Call Center 4** |
| --- | --- | --- | --- | --- |
| Service Level Agreement | 85% | 87% | 92% | 85% |
| Request Arrival Rate | 0.7684 | 0.9358 | 1.426 | 1.219 |
| Average Duration | 18.67 | 23.25 | 24.87 | 17.39 |
| Servers to meet SLA  `AGENTSB(Service Level Agreement, Request Arrival Rate, Average Duration)` | 16 | 23 | 39 | 22 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fagentsb-231ff255-172a-4586-a7de-0318c8bbea4d&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>