---
title: "ARRIVALRATE | Anapedia"
source: "https://help.anaplan.com/arrivalrate-471dcf08-90bf-4cf3-93b9-b44f66a463e6"
author:
published:
created: 2026-05-02
description: "The ARRIVALRATE function calculates the maximum interval between requests possible while processing a specified percentage of these requests."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

The ARRIVALRATE function calculates the maximum interval between requests possible while processing a specified percentage of these requests.

For example, you can use the ARRIVALRATE function to calculate how much time agents have available for other tasks.

`ARRIVALRATE(Number of servers, SLA, Target response time, Average duration)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Number of servers* | Number | The number of servers (for example, call center agents) available to process requests. |
| *SLA* | Number | The percentage of requests that need to be processed within the *Target response time*. |
| *Target response time* | Number | The time period within which each request must be responded to. |
| *Average duration* | Number | The average duration it takes to process each request. |

The ARRIVALRATE function returns a number. This is the maximum possible interval between the arrival of requests while processing the percentage of requests specified in the *SLA* argument.

Call center planning functions are unavailable in Polaris. Learn more about the differences between [Anaplan calculation engines](https://help.anaplan.com/06c06ade-2807-4f3d-9a6e-d69ae0e257e5).

The *Target response time* and *Average duration* arguments do not have to use a specific time unit. For example, they can use seconds or minutes. However, both arguments must use the same time unit.

The maximum number you can use for the *Number of servers* argument is five million.

In this example, the *Call Centers* list is on columns, and line items on rows. The first four line items contain the data for the ARRIVALRATE function for each call center:

- The number of servers available to process requests
- The percentage of calls that must be responded to within the target response time, or SLA
- The target time to respond to calls within
- The average duration it takes to complete requests

The *Arrival rate for SLA* line item uses the ARRIVALRATE function to calculate the fastest arrival rate requests can be answered within while the SLA is maintained.

The *Increased SLA* line item enables you to amend the SLA. This is used in the formula in the *Arrival rate for increased SLA* line item, which calculates the fastest arrival rate requests can be answered within while the increased SLA is maintained.

Both of the line items that contain formulas use the [**Percentage** format](https://help.anaplan.com/e7de33be-6345-4ecc-a517-c3265ff6d04a) with two decimal places to display the possibility as a percentage.

|  | **Call Center 1** | **Call Center 2** | **Call Center 3** | **Call Center 4** |
| --- | --- | --- | --- | --- |
| Number of Servers | 17 | 24 | 39 | 24 |
| Service Level Agreement | 85% | 97% | 92% | 85% |
| Target Response Time | 15 | 18 | 17 | 12 |
| Average Duration | 18.67 | 23.25 | 24.87 | 17.39 |
| Arrival rate for SLA  `ARRIVALRATE(Number of Servers, Service Level Agreement, Target Response Time, Average Duration)` | 0.8201 | 0.9481 | 1.455 | 1.266 |
| Increased SLA | 90% | 92% | 97% | 90% |
| Arrival rate for increased SLA  `ARRIVALRATE(Number of Servers, Increased SLA, Target Response Time, Average Duration)` | 0.8015 | 0.9288 | 1.413 | 1.243 |

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Farrivalrate-471dcf08-90bf-4cf3-93b9-b44f66a463e6&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>