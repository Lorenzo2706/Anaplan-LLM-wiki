---
title: "SLA | Anapedia"
source: "https://help.anaplan.com/sla-0612d0bc-6cc4-46ff-8b48-c0b501d2932b"
author:
published:
created: 2026-05-02
description: "The SLA function calculates what percentage of calls must be answered within a target answer time, or service level agreement (SLA)."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The SLA function calculates what percentage of calls must be answered within a target answer time, or service level agreement (SLA).

For example, you can use this function to ensure that enough calls are answered within a target answer time to fulfil an SLA.

`SLA(Number of servers, Target response time, Arrival rate, Average duration)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number of servers* | Number | The number of servers (for example, call center agents) available to process requests. |
| *Target response time* | Number | The time after which each request must start to be processed. |
| *Arrival rate* | Number | The interval between the arrival of each request. |
| *Average duration* | Number | The average duration it takes to process each request. |

The SLA function returns a number, which is the percentage of calls answered within the *Target response time*.

Call center planning functions are unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

The SLA is the solution to this equation:

`1- ERLANGC(x,a)e` `<sup>(a-x)t/z</sup>``, where SLA ≠ 1`

In this equation:

- x is the *Number of servers*
- a is the *Arrival rate* multiplied by the *Average duration*
- t is the *Target answer time*

The *Target response time*, *Arrival rate*, and *Average duration* arguments do not have to use a specific time unit. For example, they can be seconds or minutes. However, each argument must use the same time unit.

The maximum number you can use for the *Number of servers* argument is five million.

In this example, the *Call Centers* list is on columns, and line items on rows. The first four line items contain the data for the SLA function for each call center:

- The scheduled number of servers to process requests
- The target response time to begin processing requests within
- The interval between each request arriving
- The average duration it takes to complete requests

The fifth line item uses the SLA function to calculate what percentage of calls begin to be processed within the target response time.

The sixth line item enables you to adjust the target response time. The formula in the seventh line item uses the adjusted target response time. This enables you to see what response time it would be possible to begin processing requests in while maintaining an SLA (in this case, 95%).

Both of the line items that contain formulas use the [**Percentage** format](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) with two decimal places to display the possibility as a percentage.

|  | **Call Center 1** | **Call Center 2** | **Call Center 3** | **Call Center 4** |
| --- | --- | --- | --- | --- |
| Scheduled Number of Servers | 17 | 23 | 36 | 24 |
| Target Response Time | 15 | 18 | 17 | 12 |
| Request Arrival Rate | 0.7684 | 0.9358 | 1.426 | 1.2194 |
| Average Duration | 18.67 | 23.25 | 24.87 | 17.39 |
| Service Level Agreement  `SLA(Scheduled Number of Servers, Target Response Time, Request Arrival Rate, Average Duration)` | 95.22% | 72.50% | 37.83% | 93.39% |
| Amended Target Response Time | 15 | 50 | 135 | 14 |
| Updated SLA with amendment  `SLA(Scheduled Number of Servers, Amended Target Response Time, Request Arrival Rate, Average Duration)` | 95.22% | 95.03% | 95.10% | 95.21% |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fsla-0612d0bc-6cc4-46ff-8b48-c0b501d2932b&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>