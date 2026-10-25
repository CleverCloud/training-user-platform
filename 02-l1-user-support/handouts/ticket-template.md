# Qualified ticket — template

Copy it into `{{TICKET_TOOL}}`. A field you couldn't fill is information too: write *unknown* and why.

```text
Title:          <resource> — <symptom> (<environment>)
                e.g. "app billing-api — deployment fails at build (staging)"

Kind:           incident | request | question
Priority:       P1 | P2 | P3 | P4        (impact: …, urgency: …)

Reporter:       <name, team, contact>
Affected:       <just them | their team | several teams | everyone>

Organisation:   <name> (<orga_…>)
Resource:       <app | add-on | cluster/namespace> <name> (<id>)
Environment:    <dev | staging | prod>

Symptom:        <what happens, exact error message>
Expected:       <what should happen>
Since:          <date/time + time zone; always or intermittent>
What changed:   <deployment, variable, dependency, traffic… or "nothing known">
Impact:         <what they can't do; workaround?>

Already tried:  <by the user, by L1>
Evidence:       <commands run and their output, deployment ID, log excerpts, screenshots>

Analysis:       <what you think is happening, and why>
Next step:      <answer sent | handed over to L2 | platform team | escalated to L3> — <who, when>
```
