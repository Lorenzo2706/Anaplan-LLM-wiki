---
title: Call Center Planning Functions
type: function-category
tags: [anaplan, functions, workforce, erlang]
created: 2026-05-02
updated: 2026-05-02
---

# Call Center Planning Functions

Erlang-family workforce calculations for queue-based service operations. Inputs typically include arrival rate, average call duration, target response time, and service-level agreement (SLA) percentage.

## Members
**AGENTS, AGENTSB, ANSWERTIME, ARRIVALRATE, AVGDURATION, AVGWAIT, ERLANGB, ERLANGC, SLA**

## Variables (vocabulary)
| Symbol | Meaning |
|---|---|
| N | Number of servers / agents |
| Arr | Arrival rate (calls per unit time) |
| Dur | Average call duration |
| RT | Target response time |
| SLA | % of calls answered within RT |

## Pick your unknown
Each function fixes most variables and solves for one:

| You want to find | Function |
|---|---|
| Required agents (Erlang C) | `AGENTS(SLA, RT, Arr, Dur)` |
| Required agents in busy period (Erlang B) | `AGENTSB(SLA, Arr, Dur)` |
| Achievable SLA given resources | `SLA(N, RT, Arr, Dur)` |
| Min hold time to meet SLA | `ANSWERTIME(N, SLA, Arr, Dur)` |
| Max sustainable arrival rate | `ARRIVALRATE(N, SLA, RT, Dur)` |
| Required avg duration | `AVGDURATION(N, SLA, RT, Arr)` |
| Average waiting time | `AVGWAIT(N, Arr, Dur)` |
| Probability of being blocked (no queue) | `ERLANGB(N, Arr, Dur)` |
| Probability of being queued | `ERLANGC(N, Arr, Dur)` |

## See also
- [[wiki/functions/index]]
