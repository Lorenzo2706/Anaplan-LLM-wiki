---
title: "AVGWAIT | Anapedia"
source: "https://help.anaplan.com/avgwait-a8df0e80-d0c1-4e97-9cc1-a8b3c4b41a67"
author:
published:
created: 2026-05-02
description: "The AVGWAIT function calculates the average waiting time for a request or call to be processed."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The AVGWAIT function calculates the average waiting time for a request or call to be processed.

`AVGWAIT(Number of servers, Arrival rate, Average duration)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number of servers* (required) | Number | The number of servers (for example, call center agents) available to process requests. |
| *Arrival rate* (required) | Number | The interval between the arrival of each request. |
| *Average duration* (required) | Number | The average duration it takes to process each request. |

The AVGWAIT function returns a number. This is the average waiting time for a request to be processed, using the same time unit as the *Arrival rate* and *Average duration* arguments.

Call center planning functions are unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

The ANSWERTIME function calculates the solution to this equation:

$\text{AVGWAIT}(x,y,z) = \dfrac{(\text{ERLANGC}(x,a)*z)}{x * (1 - p)}$

In this equation:

- x is the *Number of servers*.
- y is the *Arrival rate*.
- z is the *Average duration*.
- a is the offered load, which is y multiplied by z.
- p is the offered load per server, which is a divided by x.

The *Arrival rate* and *Average duration* arguments do not have to use a specific time unit. For example, they can use seconds or minutes. However, both arguments must use the same time unit.

The maximum number you can use for the *Number of servers* argument is five million.

In this example, the *Call Centers* list is on columns, and line items on rows. The first three line items contain the data for the AVGWAIT function for each call center:

- The scheduled number of servers to process requests
- The arrival rate, or interval between each request arriving
- The average duration it takes to complete requests

The fourth line item uses the AVGWAIT function to calculate what the average waiting time for a request to be processed given the number of servers, arrival rate, and average duration to process requests.

The fifth line item enables you to adjust the arrival rate of requests. The formula in the sixth line item uses the adjusted arrival. This enables you to see how the average waiting time changes given a different arrival rate. A value of Infinity is given for *Call Center 2* because the rate of incoming requests is higher than the ability to process them, which means that calls have to wait indefinitely.

|  | **Call Center 1** | **Call Center 2** | **Call Center 3** | **Call Center 4** |
| --- | --- | --- | --- | --- |
| Scheduled Number of Servers | 25 | 45 | 50 | 39 |
| Request Arrival Rate | 0.84 | 0.93 | 0.69 | 0.68 |
| Average Duration | 25 | 46 | 45 | 45 |
| Average Waiting Time  `AVGWAIT(Scheduled Number of Servers, Request Arrival Rate, Average Duration)` | 1.9213063 | 13.4641512 | 0.00270453 | 0.53752576 |
| Adjusted Arrival Rate | 0.9 | 1.1 | 0.89 | 0.77 |
| Adjusted Average Waiting Time  `AVGWAIT(Scheduled Number of Servers, Adjusted Arrival Rate, Average Duration)` | 5.07923029 | Infinity | 0.40000875 | 3.82731801 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Favgwait-a8df0e80-d0c1-4e97-9cc1-a8b3c4b41a67&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>