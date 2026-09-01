---
title: "AGENTS | Anapedia"
source: "https://help.anaplan.com/agents-7a863c6e-0bda-4ae0-a5d9-8c9f1218d9cc"
author:
published:
created: 2026-08-31
description: "The AGENTS function calculates the minimum ‌number of servers (or agents) needed to achieve a desired Service Level."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The AGENTS function calculates the minimum ‌number of servers (or agents) needed to achieve a desired Service Level.

This function assumes the Erlang delay system, in which an unlimited queue is available and requests that can't be handled immediately wait until a server becomes available.

For example, you can use the AGENTS function to calculate the number of servers needed at peak times to maintain a certain speed of response.

`AGENTS(SLA, Target response time, Arrival rate, Average duration)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *SLA* | Number | The percentage of requests that need to be processed within the *Target response time*. |
| *Target response time* | Number | The maximum amount of time before each request starts to be processed. |
| *Arrival rate* | Number | The number of incoming requests received per unit of time. |
| *Average duration* | Number | The average amount of time it takes to process each request. |

The AGENTS function returns a number that represents the number of servers, or agents, required to process requests within the SLA.

| **Behavior** | **Classic** | **Polaris** |
| --- | --- | --- |
| When *SLA* is 0 | Returns the smallest integer above the offered load, where the offered load is equal to *Arrival rate* × *Average duration*. | Returns 0. |
| When *Average duration* is 0 | Returns NaN. | Returns 0. This is consistent with the behavior when *Arrival rate* is 0, where both engines return 0. |

The offered load must be dimensionless. This means the *Arrival rate* must be expressed per unit of time corresponding to the unit used for *Average duration*.

For example:

- If *Average duration* is measured in minutes, *Arrival rate* must be measured in requests per minute.
- If *Average duration* is measured in seconds, *Arrival rate* must be measured in requests per second.

In this example, the *Call Centers* list is on columns, and line items on rows. The first four line items contain the the percentage of calls that must be responded to within the target response time (uses the [percentage number **Format**](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a)).

The *Servers to meet SLA* line item uses the AGENTS function to calculate how many agents are needed to service the percentage of requests specified in the SLA within the target response time.

The *Amended Target Response Time* line item enables you to change the target response time. This is used in the *Updated Servers with amendment* line item, which calculates how many agents are needed to respond to requests within the amended response time while maintaining a given SLA.

|  | **Call Center 1** | **Call Center 2** | **Call Center 3** | **Call Center 4** |
| --- | --- | --- | --- | --- |
| **Service Level Agreement** | 85% | 87% | 92% | 85% |
| **Target Response Time** | 15 | 18 | 17 | 12 |
| **Request Arrival Rate** | 0.7684 | 0.9358 | 1.426 | 1.219 |
| **Average Duration** | 18.67 | 23.25 | 24.87 | 17.39 |
| **Servers to meet SLA**  `AGENTS(Service Level Agreement, Target Response Time, Request Arrival Rate, Average Duration)` | 17 | 24 | 39 | 24 |
| **Amended Target Response Time** | 10 | 10 | 10 | 10 |
| **Updated Servers with amendment**  `AGENTS(Service Level Agreement, Amended Target Response Time, Request Arrival Rate, Average Duration)` | 17 | 25 | 40 | 24 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.25.2/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;device=desktop&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fagents-7a863c6e-0bda-4ae0-a5d9-8c9f1218d9cc&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>