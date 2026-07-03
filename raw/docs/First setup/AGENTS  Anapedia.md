---
title: "AGENTS | Anapedia"
source: "https://help.anaplan.com/agents-7a863c6e-0bda-4ae0-a5d9-8c9f1218d9cc"
author:
published:
created: 2026-05-02
description: "The AGENTS function calculates the number of servers (or agents) needed to fulfil requests within a target time."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The AGENTS function calculates the number of servers (or agents) needed to fulfil requests within a target time.

For example, you can use the AGENTS function to calculate the number of servers needed at peak times to maintain a certain speed of response.

`AGENTS(SLA, Target response time, Arrival rate, Average duration)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *SLA* | Number | The percentage of requests that need to be processed within the *Target response time*. |
| *Target response time* | Number | The time period within which each request must be responded to. |
| *Arrival rate* | Number | The interval between the arrival of each request. |
| *Average duration* | Number | The average duration it takes to process each request. |

The AGENTS function returns a number, which is the number of servers, or agents, required to process requests within the SLA.

Call center planning functions are unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

The *Target response time*, *Arrival rate*, and *Average duration* arguments do not have to use a specific time unit. For example, they can use seconds or minutes. However, all three arguments must use the same time unit.

In this example, the *Call Centers* list is on columns, and line items on rows. The first four line items contain the data for the AGENTS function for each call center:

- The percentage of calls that must be responded to within the target response time, or SLA (uses the [percentage number **Format**](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a))
- The target response time to begin processing requests within
- The interval between each request arriving
- The average duration it takes to complete requests

The *Servers to meet SLA* line item uses the AGENTS function to calculate how many agents are needed to answer the percentage of calls specified in the SLA within the target response time.

The *Amended Target Response Time* line item enables you to amend the target response time. This is used in the *Updated Servers with amendment* line item, which calculates how many agents are needed to respond to requests within the amended response time while maintaining the SLA.

|  | **Call Center 1** | **Call Center 2** | **Call Center 3** | **Call Center 4** |
| --- | --- | --- | --- | --- |
| Service Level Agreement | 85% | 87% | 92% | 85% |
| Target Response Time | 15 | 18 | 17 | 12 |
| Request Arrival Rate | 0.7684 | 0.9358 | 1.426 | 1.219 |
| Average Duration | 18.67 | 23.25 | 24.87 | 17.39 |
| Servers to meet SLA  `AGENTS(Service Level Agreement, Target Response Time, Request Arrival Rate, Average Duration)` | 17 | 24 | 39 | 24 |
| Amended Target Response Time | 10 | 10 | 10 | 10 |
| Updated Servers with amendment  `AGENTS(Service Level Agreement, Amended Target Response Time, Request Arrival Rate, Average Duration)` | 17 | 25 | 40 | 24 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fagents-7a863c6e-0bda-4ae0-a5d9-8c9f1218d9cc&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>