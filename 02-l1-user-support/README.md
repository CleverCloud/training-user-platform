# User support and qualifying user needs — Session 2

Support L1 training, hands-on: a developer opens a ticket, you qualify it, then you find the answer in the logs and the Console. One app, five scenarios — the normal case, then things going wrong.

**Duration:** 2 hours, mostly hands-on · **Audience:** L1/L2 support engineers and platform operators

## Contents

| | |
|---|---|
| [`prerequisites.md`](prerequisites.md) | What must be ready: platform access, quota, Clever Tools logged in |
| [`lab.md`](lab.md) | The lab, scenario by scenario |
| [`demos/`](demos/) | The app (`1-base/`) and the overlays for scenarios 2 to 5 |
| [`handouts/qualification-checklist.md`](handouts/qualification-checklist.md) | The questions to ask, and the identifiers to collect, for any platform ticket |
| [`handouts/ticket-template.md`](handouts/ticket-template.md) | What a qualified ticket contains |
| [`slides/`](slides/) | The session's slides, in English and French (PDF) |

Placeholders such as `{{ORG_NAME}}`, `{{L3_CONTACT}}` or `{{TICKET_TOOL}}` depend on your organisation: your trainer gives you the values.

## Why this session

Developers rarely start with a clear question: *"it doesn't work"*, *"the platform is down"*, *"the database is broken"*. The first job of L1 is to **understand** — then to look in the right place. In this lab you play both sides: you deploy and break a real app the way developers do, then you investigate their tickets. Most of the time, the platform is working fine and the answer is in the logs.

## Learning objectives

At the end of the session, you can:

1. Place L1 in the support chain (developer → L1 → L2 → L3 at Clever Cloud) and say what L1 resolves, routes and escalates.
2. Tell an incident ("it's broken") from a request ("I need…") and a question ("how do I…").
3. Qualify an incident: what, who, where, since when, what changed, impact — and collect the platform identifiers (organisation, app or add-on ID, cluster and namespace, deployment ID, time range).
4. Find the answer in the right place: deployment logs, runtime logs, the add-on's limits and dashboard, the app's configuration (`clever activity`, `clever logs`, `clever env`, `clever addon env`, the Console).
5. Recognise the classic causes: a failed build (previous version still serving), a resource limit (connections), ephemeral local disk, a misconfigured mount — and explain them to a developer.
6. Set a priority from impact and urgency, and route: answer yourself, hand over to L2 or the platform team, escalate to L3.
7. Write a clear reply to the user and a complete escalation.

## Agenda

1. Setup check — and the support mindset: ticket → qualify → look
2. **Scenario 1** — the normal case: a Python app and its PostgreSQL database
3. **Scenario 2** — "my change isn't online": a deployment that fails
4. **Scenario 3** — "it works, then it errors": the limits of an add-on
5. **Scenario 4** — "my files disappear": persistent storage with an FS Bucket
6. **Scenario 5** — "files vanish again": a misconfiguration with no error message
7. Debrief: what each ticket taught, how to write it down

## Key messages

1. **Understand before you fix.** The first message is a symptom, rarely the problem — and "the platform is down" rarely means the platform is down.
2. **No identifiers, no ticket.** Organisation, app or add-on ID, environment, time range: without them nobody — at any level — can look.
3. **"What changed?"** is the most useful question in support: a deployment, a variable, a dependency, the traffic.
4. **Look in the right log.** Build and start problems are in the **deployment log**; errors after start are in the **runtime logs**; limits are in the **add-on** (plan, dashboard).
5. **A failed deployment doesn't take the app down**: the previous version keeps serving. "My change isn't online" is a deployment to read, not an outage.
6. **A restart is not a fix.** If restarting "helps for a minute", something is accumulating: connections, memory, files.
7. **No error is also a symptom.** A mount silently ignored, files written to the wrong folder: compare what is configured with what actually happens.
8. **One user or everyone?** Scope decides priority and routing: one app is a ticket for L1/L2, every team blocked is an incident to escalate now — with a package, not a forward.

## Documentation

- Clever Cloud documentation: <https://www.clever.cloud/developers/doc/>
- Troubleshooting: <https://www.clever.cloud/developers/doc/find-help/troubleshooting/>
- Clever Tools CLI reference: <https://www.clever.cloud/developers/doc/cli-reference/>
