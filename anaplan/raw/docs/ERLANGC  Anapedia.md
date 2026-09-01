---
title: "ERLANGC | Anapedia"
source: "https://help.anaplan.com/erlangc-c1845a89-a6af-4569-93c0-b67d76dd6649"
author:
published:
created: 2026-08-31
description: "The ERLANGC function calculates the probability that a request will be placed in a queue given a specified number of servers, the arrival rate of requests, and the average time to service a request."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The ERLANGC function calculates the probability that a request will be placed in a queue given a specified number of servers, the arrival rate of requests, and the average time to service a request.

This function assumes the Erlang delay system, in which an unlimited queue is available and requests that can't be handled immediately wait until a server becomes available.

For example, you can use the ERLANGC function to estimate the probability that an incoming call to a call center is placed in a queue because all agents are busy.

`ERLANGC(Number of servers, Arrival rate, Average duration)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number of servers* | Number | The number of servers (for example, call center agents) available to process requests. |
| *Arrival rate* | Number | The number of incoming requests received per unit of time. |
| *Average duration* | Number | The average amount of time it takes to process each request. |

The ERLANGC function returns a number that represents the probability that a request is placed in a queue.

| **Behavior** | **Classic** | **Polaris** |
| --- | --- | --- |
| Rounding of the number of agents | Truncates the number of agents by rounding it toward 0.  For example, 1.5 becomes 1 and -1.5 becomes -1. | Rounds the number of agents to the nearest integer, with halves rounded away from 0.  For example, 1.5 becomes 2 and -1.5 becomes -2. |
| When *Arrival rate* is 0 | Returns NaN if *Number of servers* is a negative value and 0 otherwise. | Returns 0 regardless of the value of *Number of servers.* |
| When *Average duration* is 0 | Always returns NaN. | Always returns 0. |

ERLANGC is defined by this formula:

$$
\operatorname{ERLANGC}(m,\lambda,\mu) = \dfrac{\frac{\alpha^m}{m!}}{\frac{\alpha^m}{m!}+(1-\rho)\displaystyle\sum_ {k=0}^{m-1} \frac{\alpha^k}{k!}}
$$

where:

- *m* is the *Number of servers*
- *λ* is the *Arrival rate*
- *μ* is the *Average duration*
- *α* is the offered load, equal to *λ* × *μ*
- *ρ* is the offered load per server, which is *α* divided by *m*

The offered load must be dimensionless. This means the *Arrival rate* must be expressed per unit of time corresponding to the unit used for *Average duration*.

For example:

- If *Average duration* is measured in minutes, *Arrival rate* must be measured in requests per minute.
- If *Average duration* is measured in seconds, *Arrival rate* must be measured in requests per second.

The maximum number you can use for the *Number of servers* argument is five million.

In this example, the *Call Centers* list is on columns, and line items on rows. The first three line items contain the scheduled number of servers, arrival rate of requests, and average time to service a request. The fourth line item, *Busy Probability* calculates the probability of a call entering a queue using the ERLANGC formula.

The final two line items are a numeric line item, *Extra Agents*, to adjust the number of servers, and a formula that displays the busy probability after adjustment.

The example shows how the number of agents can be adjusted until the desired busy probability is reached (in this case, less than 15%). In practice, [AGENTS](https://help.anaplan.com/7a863c6e-0bda-4ae0-a5d9-8c9f1218d9cc) can be used to automatically calculate the minimum number of agents required to meet a target SLA.

Both of the line items that contain formulas use the [**Percentage** format](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) with two decimal places to display the probability as a percentage.

The arrival rate and average duration must use the same compatible units. In this example, the arrival rate is measured in requests per minute and the average duration is measured in minutes, so their product (the offered load) is dimensionless.

|  | **Call Center 1** | **Call Center 2** | **Call Center 3** | **Call Center 4** |
| --- | --- | --- | --- | --- |
| **Scheduled Number of Agents** | 33 | 50 | 55 | 40 |
| **Request Arrival Rate** | 0.76 | 0.87 | 1.35 | 2.81 |
| **Average Duration** | 19.25 | 52.9 | 34.9 | 13.1 |
| **Busy Probability**  `ERLANGC(Scheduled Number of Agents, Request Arrival Rate, Average Duration)` | 0.0026% | 46% | 18.9% | 50.41% |
| **Extra Agents** | \-13 | 5 | 1 | 5 |
| **Amended Busy Probability**  `ERLANGC(Scheduled Number of Agents + Extra Agents, Request Arrival Rate, Average Duration)` | 13.3% | 13.9% | 14.7% | 13.48% |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.25.2/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;device=desktop&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ferlangc-c1845a89-a6af-4569-93c0-b67d76dd6649&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>