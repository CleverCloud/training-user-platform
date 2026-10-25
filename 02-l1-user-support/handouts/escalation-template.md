# Escalation — template

An escalation is a **package**, not a forward. The next level must be able to start working without asking you anything.

```text
To:             L2 | platform team | L3 Clever Cloud ({{L3_CONTACT}})
Ticket:         <your ticket ID and link>
Priority:       P1–P4 — <why>

Summary:        <one sentence: what is broken, for whom, since when>

Scope:          <one app | one team | several teams | all users> — <how you know>
Resource(s):    <organisation, app/add-on/cluster IDs, environment>
Time range:     <start – now, time zone>

What we checked:
  - <check 1> → <result>
  - <check 2> → <result>
Evidence:       <deployment IDs, log excerpts with timestamps, command outputs — attached>

What we think:  <hypothesis, or "no hypothesis">
What we need:   <a fix | an analysis | a confirmation | an answer by …>
Contact:        <who to call back, availability>
```

**Before escalating to L3**, check: is it really the platform (several unrelated apps or teams, platform components, not reproducible as a usage mistake)? Is it already known (status page, incident channel, other tickets)?
