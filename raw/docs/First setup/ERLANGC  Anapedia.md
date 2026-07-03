---
title: "ERLANGC | Anapedia"
source: "https://help.anaplan.com/erlangc-c1845a89-a6af-4569-93c0-b67d76dd6649"
author:
published:
created: 2026-05-02
description: "The ERLANGC function determines the probability of a request being placed in a queue given a specified number of servers, arrival rate of requests, and the average duration to process requests."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The ERLANGC function determines the probability of a request being placed in a queue given a specified number of servers, arrival rate of requests, and the average duration to process requests.

For example, you can use the ERLANGC function to ensure that a certain percentage do not enter a queue.

`ERLANGC(Number of servers, Arrival rate, Average duration)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number of servers* | Number | The number of servers (for example, call center agents) available to process requests. |
| *Arrival rate* | Number | The interval between the arrival of each request. |
| *Average duration* | Number | The average duration it takes to process each request. |

The ERLANGC function returns a number, which is the probability a request is placed in an infinite queue.

Call center planning functions are unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

Erlang C is the solution to this equation:

$ERLANG-C(x,y,z) = \dfrac{\frac{\alpha^x}{x!}}{\frac{\alpha^x}{x!}+(1-\rho)\displaystyle\sum_ {k=0}^{x-1} \frac{\alpha^k}{k!}}$

In this equation:

- x is the *Number of servers*.
- y is the *Arrival rate*.
- z is the *Average duration*.
- a is the offered load, which is y multiplied by z.
- p is the offered load per server, which is a divided by x.

The *Arrival rate* and *Average duration* arguments do not have to use a specific time unit. For example, they can be seconds or minutes. However, both arguments must use the same time unit.

The maximum number you can use for the *Number of servers* argument is five million.

In this example, the *Call Centers* list is on columns, and line items on rows. The first three line items contain the scheduled number of servers, arrival rate of requests, and average duration to fulfil requests. The fourth line item, *Queuing Possibility* calculates the possibility of a call entering a queue using a formula.

The final two line items are a numeric line item, *Extra Agents*, to adjust the number of servers, and a formula that displays the blocking possibility after adjustment. This can be used to adjust the number of servers until the desired blocking possibility is reached (in this case, less than 15%).

Both of the line items that contain formulas use the [**Percentage** format](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) with two decimal places to display the possibility as a percentage.

|  | **Call Center 1** | **Call Center 2** | **Call Center 3** | **Call Center 4** |
| --- | --- | --- | --- | --- |
| Scheduled Number of Agents | 33 | 50 | 55 | 40 |
| Request Arrival Rate | 0.76 | 0.87 | 1.35 | 2.81 |
| Average Duration | 19.25 | 52.9 | 34.9 | 13.1 |
| Queuing Possibility  `ERLANGC(Scheduled Number of Agents, Request Arrival Rate, Average Duration)` | 0.00% | 46.04% | 18.93% | 50.41% |
| Extra Agents | \-13 | 5 | 1 | 5 |
| Amended Queuing Possibility  `ERLANGC(Scheduled Number of Agents + Extra Agents, Request Arrival Rate, Average Duration)` | 13.26% | 13.93% | 14.65% | 13.48% |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ferlangc-c1845a89-a6af-4569-93c0-b67d76dd6649&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>