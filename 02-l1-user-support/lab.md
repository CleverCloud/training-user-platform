# Session 2 — Lab: from a ticket to the logs

One app, five scenarios. In each one, a developer opens a ticket; you qualify it with the [qualification checklist](handouts/qualification-checklist.md), then find the answer **in the logs and the Console**.

Replace `<your-name>` by your first name (lowercase, no spaces).

## Your platform

| Parameter | Value |
|-----------|-------|
| Console | `{{CONSOLE_URL}}` |
| Organisation | `{{ORG_NAME}}` |
| Zone (region) | `{{ZONE}}` |
| Application domain | `{{APP_DOMAIN}}` |

---

## Scenario 0 — Is your setup working? (10 min)

```bash
git --version
clever version
clever profile                               # your account, the right API host
clever applications list --org {{ORG_NAME}}  # works, even if empty
```

Open the Console in your browser and select `{{ORG_NAME}}`. Blocked? Say it now — it's your first support ticket of the day: qualify it with the trainer.

---

## Scenario 1 — The normal case (25 min)

This is how things should go. Take your time: every following scenario builds on this app.

```bash
cp -r <session-folder>/demos/1-base ~/cc-support-<your-name>
cd ~/cc-support-<your-name>
git init && git add . && git commit -m "v1"

clever create --type python --org {{ORG_NAME}} --region {{ZONE}} support-<your-name>
clever addon create postgresql-addon pg-<your-name> --plan dev --org {{ORG_NAME}} --region {{ZONE}}
clever service link-addon pg-<your-name>
clever env set CC_PYTHON_MODULE app:app

clever deploy
```

Then:

```bash
clever domain
curl https://<your-app-domain>/          # version v1
curl https://<your-app-domain>/db        # visits counter
clever activity
clever logs --since 10m
```

Note for later — you'll need them in every ticket: your **organisation ID**, **app ID**, **add-on ID** (Console → Information, or `clever status` / `clever addon list --org {{ORG_NAME}}`).

---

## Scenario 2 — "My change isn't online" (15 min)

→ [`demos/2-no-deploy/`](demos/2-no-deploy/)

## Scenario 3 — "It works, then it errors" (20 min)

→ [`demos/3-connections/`](demos/3-connections/)

## Scenario 4 — "My files disappear": add an FS Bucket (20 min)

→ [`demos/4-fs-bucket/`](demos/4-fs-bucket/)

## Scenario 5 — "Files vanish again" (15 min)

→ [`demos/5-fs-bucket-config/`](demos/5-fs-bucket-config/)

---

## For each ticket, write it down

Fill the [ticket template](handouts/ticket-template.md) — kind, priority, identifiers, evidence, analysis, next step — as if you had to hand it over to someone else. The debrief uses it.

## Clean up

*Unless the trainer asks you to keep your resources for the next session.*

```bash
clever service unlink-addon pg-<your-name>
clever service unlink-addon fs-<your-name>
clever addon delete pg-<your-name> --org {{ORG_NAME}}
clever addon delete fs-<your-name> --org {{ORG_NAME}}
clever delete
```

## Cheat sheet

| I want to… | Command |
|------------|---------|
| app status / deployment history | `clever status` · `clever activity` |
| logs of one deployment | `clever logs --deployment-id <id>` |
| runtime logs | `clever logs --since 30m [--search <text>]` |
| access logs | `clever accesslogs --since 30m` |
| app / add-on variables | `clever env` · `clever addon env <addon-id>` |
| redeploy / rebuild | `clever restart` · `clever restart --without-cache` |
| list add-ons | `clever addon list --org {{ORG_NAME}}` |
| info for support | `clever diag` |
