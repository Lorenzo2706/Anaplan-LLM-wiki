---
title: "ERLANGB | Anapedia"
source: "https://help.anaplan.com/erlangb-207c6b4f-3ca6-4bad-ac7c-6f040fd555c3"
author:
published:
created: 2026-08-31
description: "The ERLANGB function calculates the probability that a request will be blocked given a specified number of servers, the arrival rate of requests, and the average time to service a request."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The ERLANGB function calculates the probability that a request will be blocked given a specified number of servers, the arrival rate of requests, and the average time to service a request.

This function assumes the Erlang loss system, in which no queue exists and requests that can't be handled immediately are blocked rather than queued.

For example, you can use the ERLANGB function to estimate the probability that an incoming call to a call center is blocked because all agents are busy.

`ERLANGB(Number of servers, Arrival rate, Average duration)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number of servers* | Number | The number of servers (for example, call center agents) available to process requests. |
| *Arrival rate* | Number | The number of incoming requests received per unit of time. |
| *Average duration* | Number | The average amount of time it takes to process each request. |

The ERLANGB function returns a number that represents the probability that a request is blocked.

| **Behavior** | **Classic** | **Polaris** |
| --- | --- | --- |
| Rounding of the number of agents | Truncates the number of agents by rounding it toward 0.  For example, 1.5 becomes 1 and -1.5 becomes -1. | Rounds the number of agents to the nearest integer, with halves rounded away from 0.  For example, 1.5 becomes 2 and -1.5 becomes -2. |
| When *Arrival rate* is 0 | Returns NaN if *Number of servers* is a negative value and 0 otherwise. | Returns 0 regardless of the value of *Number of servers.* |
| When *Average duration* is 0 | Always returns NaN. | Always returns 0. |

ERLANGB is defined by this formula:

$$
\operatorname{ERLANGB}(m,\lambda,\mu) = \dfrac{\frac{\alpha^m}{m!}}{\displaystyle\sum^{k = m}_{k = 0}\frac{\alpha^k}{k!}}
$$

where:

- *m* is the *Number of servers*
- *λ* is the *Arrival rate*
- *μ* is the *Average duration*
- *α* is the offered load, equal to *λ* × *μ*

The offered load must be dimensionless. This means the *Arrival rate* must be expressed per unit of time corresponding to the unit used for *Average duration*.

For example:

- If *Average duration* is measured in minutes, *Arrival rate* must be measured in requests per minute.
- If *Average duration* is measured in seconds, *Arrival rate* must be measured in requests per second.

The maximum number you can use for the *Number of servers* argument is five million.

In this example, the *Call Centers* list is on columns, and line items on rows. The first three line items contain the scheduled number of servers, arrival rate of requests, and average time to service a request. The fourth line item, *Busy Probability*, calculates the probability of a call being blocked using the ERLANGB formula.

The final two line items are a numeric line item, *Extra Servers*, to adjust the number of servers, and a formula that displays the busy probability after adjustment.

The example shows how the number of agents can be adjusted until the desired busy probability is reached (in this case, less than 5%). In practice, [AGENTSB](https://help.anaplan.com/231ff255-172a-4586-a7de-0318c8bbea4d) can be used to automatically calculate the minimum number of agents required to meet a target SLA.

Both of the line items that contain formulas use the [**Percentage** format](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) with two decimal places to display the probability as a percentage.

The arrival rate and average duration must use the same compatible units. In this example, the arrival rate is measured in requests per minute and the average duration is measured in minutes, so their product (the offered load) is dimensionless.

|  | **Call Center 1** | **Call Center 2** | **Call Center 3** | **Call Center 4** |
| --- | --- | --- | --- | --- |
| **Scheduled Number of Servers** | 25 | 45 | 50 | 39 |
| **Request Arrival Rate** | 0.76 | 0.93 | 1.4 | 1.2 |
| **Average Duration** | 25 | 55 | 45 | 66 |
| **Busy Probability**  `ERLANGB(Scheduled Number of Servers, Request Arrival Rate, Average Duration)` | 3.63% | 18.6% | 24.7% | 51.88% |
| **Extra Servers** | \-1 | 12 | 19 | 46 |
| **Amended Busy Probability**  `ERLANGB(Scheduled Number of Servers + Extra Servers, Request Arrival Rate, Average Duration)` | 4.95% | 4.69% | 4.57% | 4.60% |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.25.2/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;device=desktop&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Ferlangb-207c6b4f-3ca6-4bad-ac7c-6f040fd555c3&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>