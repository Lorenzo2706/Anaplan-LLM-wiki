---
title: "ERLANGB | Anapedia"
source: "https://help.anaplan.com/erlangb-207c6b4f-3ca6-4bad-ac7c-6f040fd555c3"
author:
published:
created: 2026-05-02
description: "The ERLANGB function determines the probability of a request being blocked given a specified number of servers, arrival rate of requests, and the average service duration."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The ERLANGB function determines the probability of a request being blocked given a specified number of servers, arrival rate of requests, and the average service duration.

For example, you can use the ERLANGB function to ensure that a certain percentage of all requests are fulfilled.

`ERLANGB(Number of servers, Arrival rate, Average duration)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number of servers* | Number | The number of servers (for example, call center agents) available to process requests. |
| *Arrival rate* | Number | The interval between the arrival of each request. |
| *Average duration* | Number | The average duration it takes to process each request. |

The ERLANGB function returns a number, which is the probability a request is blocked.

Call center planning functions are unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

Erlang B is the solution to this equation:

$ERLANGB(x,y,z) = \dfrac{\frac{\alpha^x}{x!}}{\displaystyle\sum^{k = x}_{k = 0}\frac{\alpha^k}{k!}}$

In this equation:

- x is the *Number of servers*.
- y is the *Arrival rate*.
- z is the *Average duration*.
- a is the offered load, which is y multiplied by z.

The *Arrival rate* and *Average duration* arguments do not have to use a specific time unit. For example, they can use seconds or minutes. However, both arguments must use the same time unit.

The maximum number you can use for the *Number of servers* argument is five million.

In this example, the *Call Centers* list is on columns, and line items on rows. The first three line items contain the scheduled number of servers, arrival rate of requests, and average duration to fulfil requests. The fourth line item, *Blocking Possibility* calculates the possibility of a call being blocked using a formula.

The final two line items are a numeric line item, *Required Extra Agents*, to adjust the number of servers, and a formula that displays the blocking possibility after adjustment. This can be used to adjust the number of servers until the desired blocking possibility is reached (in this case, less than 5%).

Both of the line items that contain formulas use the [**Percentage** format](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) with two decimal places to display the possibility as a percentage.

|  | **Call Center 1** | **Call Center 2** | **Call Center 3** | **Call Center 4** |
| --- | --- | --- | --- | --- |
| Scheduled Number of Servers | 25 | 45 | 50 | 39 |
| Request Arrival Rate | 0.76 | 0.93 | 1.4 | 1.2 |
| Average Duration | 25 | 55 | 45 | 66 |
| Blocking Possibility  `ERLANGB(Scheduled Number of Servers, Request Arrival Rate, Average Duration)` | 3.63% | 18.58% | 24.74% | 51.88% |
| Extra Servers | \-1 | 12 | 19 | 46 |
| Amended Blocking Possibility  `ERLANGB(Scheduled Number of Servers + Required Extra Servers, Request Arrival Rate, Average Duration)` | 4.85% | 4.69% | 4.57% | 4.60% |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ferlangb-207c6b4f-3ca6-4bad-ac7c-6f040fd555c3&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>