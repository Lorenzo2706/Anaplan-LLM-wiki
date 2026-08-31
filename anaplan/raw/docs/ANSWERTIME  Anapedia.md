---
title: "ANSWERTIME | Anapedia"
source: "https://help.anaplan.com/answertime-e4c87efc-cfb3-4bd0-8d40-6633407f8f5d"
author:
published:
created: 2026-05-02
description: "The ANSWERTIME function calculates the minimum hold time required to answer a certain percentage of calls, or service level agreement (SLA)."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The ANSWERTIME function calculates the minimum hold time required to answer a certain percentage of calls, or service level agreement (SLA).

For example, you can use the ANSWERTIME function to adjust the hold time during busy periods.

`ANSWERTIME(Number of servers, SLA, Arrival rate, Average duration)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number of servers* | Number | The number of servers (for example, call center agents) available to process requests. |
| *SLA* | Number | The percentage of requests that need to be processed. |
| *Arrival rate* | Number | The interval between the arrival of each request. |
| *Average duration* | Number | The average duration it takes to process each request. |

The ANSWERTIME function returns a number, which is the minimum hold time required to answer the percentage of calls specified in the *SLA* argument.

Call center planning functions are unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

The ANSWERTIME function calculates the solution to this equation:

$\text{ANSWERTIME}(x,w,y,z) = \dfrac{z\left(\text{log}(1-w) - \text{log}(\text{ERLANGC}(x,y,z))\right)}{a - x}$

In this equation:

- x is the *Number of servers*.
- w is the *SLA*.
- y is the *Arrival rate*.
- z is the *Average duration*.
- a is the offered load, which is y multiplied by z.

The *Arrival rate* and *Average duration* arguments do not have to use a specific time unit. For example, they can use seconds or minutes. However, both arguments must use the same time unit.

The maximum number you can use for the *Number of servers* argument is five million.

In this example, the *Call Centers* list is on columns, and line items on rows. The first four line items contain the data for the ANSWERTIME function for each call center:

- The number of servers available to process requests
- The percentage of calls that must be responded to within the target response time, or SLA
- The interval between each request arriving
- The average duration it takes to complete requests

The *Answer time for SLA* line item uses the ANSWERTIME function to calculate how quickly requests are responded to given the number of agents, SLA, arrival rate, and average duration.

The *Increased SLA* line item enables the user of the module to amend the SLA. This is used in formula in the *Answer time for increased SLA* line item, which calculates how quickly requests are responded to given the number of agents, SLA, arrival rate, and average duration.

Both of the line items that contain SLAs use the [**Percentage** format](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) with two decimal places.

|  | **Call Center 1** | **Call Center 2** | **Call Center 3** | **Call Center 4** |
| --- | --- | --- | --- | --- |
| Number of Servers | 17 | 24 | 39 | 24 |
| Service Level Agreement | 85% | 87% | 92% | 85% |
| Request Arrival Rate | 0.7684 | 0.9358 | 1.426 | 1.2194 |
| Average Duration | 18.67 | 23.25 | 24.87 | 17.39 |
| Answer time for SLA  `ANSWERTIME(Number of Servers, Service Level Agreement, Request Arrival Rate, Average Duration)` | 6.949 | 14.8 | 12.27 | 6.902 |
| Increased SLA | 90% | 82% | 97% | 90% |
| Answer time for increased SLA  `ANSWERTIME(Number of Servers, Increased SLA, Request Arrival Rate, Average Duration)` | 9.802 | 19.83 | 19.17 | 9.425 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fanswertime-e4c87efc-cfb3-4bd0-8d40-6633407f8f5d&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>