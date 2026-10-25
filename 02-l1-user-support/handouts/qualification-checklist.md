# Qualification checklist

Use it on every ticket, before trying to fix anything. You don't need every answer — you need to know which ones are missing.

## 1. What kind of ticket?

| Kind | The user says… | Goal |
|------|----------------|------|
| **Incident** | "It's broken", "it doesn't work anymore", "it's slow", "I get an error" | Restore service |
| **Request** | "I need…", "can I have…", "please create…" | Find the right offer, provide it or route it |
| **Question** | "How do I…?", "is it possible to…?", "why does…?" | Answer, point to the documentation |

A ticket can change kind while you qualify it: "I need a VM" (request) often hides "my build fails because a library is missing" (incident).

## 2. The questions (incident)

| | Question | Why |
|---|---|---|
| **What** | What exactly happens? What did you expect? Exact error message, screenshot, URL? | A symptom you can observe yourself |
| **Who** | Who is affected: you, your team, several teams, everyone? | Scope → priority, and platform vs app |
| **Where** | Which organisation, which app / add-on / cluster + namespace? Which environment (dev, staging, prod)? | Without the resource, nobody can look |
| **When** | Since when? Always, or intermittently? Exact time of the last failure (with time zone)? | Time range for logs and activity |
| **What changed** | A deployment, a variable, a dependency, a configuration, more traffic, a new team member? | The most frequent cause, by far |
| **Impact** | What can't you do? Is production affected? Is there a workaround? | Priority |
| **Tried** | What have you already tried? | Avoid repeating, and spot side effects |

## 3. The identifiers to collect

| Resource | Identifier | Where the user finds it |
|----------|------------|-------------------------|
| Organisation | name and ID (`orga_…`) | Console → organisation → Information |
| Application | name and ID (`app_…`) | Console → app → Information; `.clever.json` in the project; `clever status` |
| Add-on | name and ID (`addon_…`, or `postgresql_…`, `redis_…`…) | Console → add-on → Information; `clever addon list` |
| Deployment | deployment ID, commit ID, time | `clever activity`; Console → Activity |
| Instance | instance number / ID | `clever instances`; the app's own logs |
| CKE | cluster name, namespace, workload name | `clever k8s list`; `kubectl get pods -n <namespace>` |
| User's setup | Clever Tools version, OS, network (proxy, VPN) | `clever diag` |

## 4. What to ask the user to run (and send back)

| Situation | Command | What you look for |
|-----------|---------|-------------------|
| Any app issue | `clever status` · `clever activity` | Running or not, last deployments and their result |
| Deployment failed | `clever logs --deployment-id <id>` (or the Console's deployment logs) | The step that failed and its error |
| App errors at runtime | `clever logs --since 1h` | Stack traces, restarts |
| HTTP errors, slowness | `clever accesslogs --since 1h` | Status codes, response times, which paths |
| CLI problem | `clever diag` · `clever version` | Version, OS, configuration, API host |
| CKE workload | `kubectl get pods -n <ns>` · `kubectl describe pod <pod> -n <ns>` · `kubectl get events -n <ns>` | Status (Pending, CrashLoopBackOff…) and its reason |

## 5. Priority

Generic matrix — replace with your organisation's scale (`{{PRIORITY_SCALE}}`).

| Impact \ Urgency | Blocking now, no workaround | Degraded, workaround exists | Can wait |
|---|---|---|---|
| **Many teams / production** | P1 | P2 | P3 |
| **One team / one app in production** | P2 | P3 | P3 |
| **One user / non-production** | P3 | P4 | P4 |

## 6. Route

- **Answer it yourself (L1):** questions, requests covered by self-service and the docs, incidents caused by the user's app or configuration with a known fix.
- **Hand over to L2:** incidents you can't explain after qualification, advanced troubleshooting, anything needing deeper platform access.
- **Platform team:** CKE cluster capacity, node groups, quotas, namespaces and access; organisation-level settings.
- **Escalate to L3 (Clever Cloud):** suspected platform defect or platform-wide incident — through `{{L3_CONTACT}}`, with a complete escalation (see `escalation-template.md`).
