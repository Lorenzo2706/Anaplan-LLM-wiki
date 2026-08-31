---
title: "AVGDURATION | Anapedia"
source: "https://help.anaplan.com/avgduration-8f1849a0-256f-4700-8c4a-82cfa5e50d7d"
author:
published:
created: 2026-05-02
description: "The AVGDURATION function calculates the required average duration of calls in order to answer a certain percentage of calls, or service level agreement (SLA)."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The AVGDURATION function calculates the required average duration of calls in order to answer a certain percentage of calls, or service level agreement (SLA).

`AVGDURATION(Number of servers, SLA, Target response time, Arrival rate)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number of servers* (required) | Number | The number of servers (for example, call center agents) available to process requests. |
| *SLA* (required) | Number | The percentage of requests that need to be processed within the *Target response time*. |
| *Target response time* (required) | Number | The time after which each request must start to be processed. |
| *Arrival rate* (required) | Number | The interval between the arrival of each request. |

The AVGDURATION function returns a number. This is the average duration it takes to process requests, using the same time unit as the *Target response time* and *Arrival rate* arguments.

Call center planning functions are unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

The *Target response time* and *Arrival rate* arguments do not have to use a specific time unit. For example, they can be seconds or minutes. However, each argument must use the same time unit.

The maximum number you can use for the *Number of servers* argument is five million.

In this example, the *Call Centers* list is on columns, and line items on rows. The first four line items contain the data for the AVGDURATION function for each call center:

- The scheduled number of servers to process requests
- The percentage of calls that must be responded to within the target response time, or SLA
- The target response time to begin processing requests within
- The arrival rate, or interval between each request arriving

The fifth line item uses the AVGDURATION function to calculate what the average duration of call is given the number of servers, SLA, target response time, and arrival rate of calls.

The sixth line item enables you to adjust the SLA. The formula in the seventh line item uses the adjusted SLA. This enables you to see how the average duration of calls changes given a different SLA.

Both of the line items that contain SLAs use the [**Percentage** format](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) with two decimal places.

|  | **Call Center 1** | **Call Center 2** | **Call Center 3** | **Call Center 4** |
| --- | --- | --- | --- | --- |
| Scheduled Number of Agents | 16 | 22 | 37 | 23 |
| SLA | 85.00% | 87.00% | 92.00% | 85.00% |
| Target Response Time | 15 | 18 | 17 | 12 |
| Arrival Rate | 0.7673 | 0.9621 | 1.428 | 1.213 |
| Average Duration  `AVGDURATION(Scheduled Number of Agents, SLA, Target Response Time, Arrival Rate)` | 18.67 | 21 | 24 | 17.34 |
| Amended SLA | 90.00% | 92.00% | 97.00% | 90.00% |
| Amended Average Duration  `AVGDURATION(Scheduled Number of Agents, Amended SLA, Target Response Time, Arrival Rate)` | 18.26 | 20.6 | 23.35 | 17.04 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Favgduration-8f1849a0-256f-4700-8c4a-82cfa5e50d7d&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>