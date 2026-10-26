# Session 2 — Lab: from a ticket to the logs

One app, five scenarios. In each one, a developer opens a ticket; you qualify it with the [qualification checklist](handouts/qualification-checklist.md), then find the answer **in the logs and the Console**.

Replace `<your-name>` by your first name (lowercase, no spaces).

## Your platform

| Parameter | Value |
|-----------|-------|
| Console | `{{CONSOLE_URL}}` |
| Organisation | `{{ORG_NAME}}` |
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

First, tell your shell where this session's folder is (the folder holding `lab.md` and `demos/`): every scenario uses it.

```bash
export LAB=<session-folder>          # e.g. export LAB=~/training/02-l1-user-support
ls $LAB/demos                        # 1-base  2-no-deploy  3-connections  4-fs-bucket  5-fs-bucket-config
```

> New terminal? Run the `export LAB=…` line again.

Then create and deploy the app:

```bash
cp -r $LAB/demos/1-base ~/cc-support-<your-name>
cd ~/cc-support-<your-name>
git init && git add . && git commit -m "v1"

clever create --type python --org {{ORG_NAME}} support-<your-name>
clever addon create postgresql-addon pg-<your-name> --plan dev --org {{ORG_NAME}}
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
clever logs --since 10m --until now
```

Note for later — you'll need them in every ticket: your **organisation ID**, **app ID**, **add-on ID** (Console → Information, or `clever status` / `clever addon list --org {{ORG_NAME}}`).

---

## How the next scenarios work

Each scenario is a **new release of your app**, prepared by "the developer": you copy its files over your app, commit, deploy — then a ticket arrives. Always from your app folder:

```bash
cd ~/cc-support-<your-name>
cp -R $LAB/demos/<scenario>/files/. .       # the new release
git add -A && git commit -m "<scenario>"
clever deploy
```

Then read the ticket and investigate. Start from the ticket and the logs, not from the diff.

---

## Scenario 2 — "My change isn't online" (15 min)

```bash
cd ~/cc-support-<your-name>
cp -R $LAB/demos/2-no-deploy/files/. .
git add -A && git commit -m "v2"
clever deploy                                # watch what happens
```

> **Ticket:** *"I pushed version 2 of the app an hour ago and it still shows version 1! Is the platform down?"*

Questions and hints: [`demos/2-no-deploy/`](demos/2-no-deploy/).

## Scenario 3 — "It works, then it errors" (20 min)

```bash
cd ~/cc-support-<your-name>
cp -R $LAB/demos/3-connections/files/. .
git add -A && git commit -m "v3"
clever deploy
for i in $(seq 1 10); do curl -s -o /dev/null -w "%{http_code}\n" https://<your-app-domain>/db; done
```

> **Ticket:** *"Since this morning's release, `/db` works for a few calls, then only returns errors. Restarting the app fixes it for a minute. Is the database broken?"*

Questions and hints: [`demos/3-connections/`](demos/3-connections/).

## Scenario 4 — "My files disappear": add an FS Bucket (20 min)

```bash
cd ~/cc-support-<your-name>
cp -R $LAB/demos/4-fs-bucket/files/. .
git add -A && git commit -m "v4"
clever deploy
```

**Step 1 — See the problem**

```bash
curl -X POST --data "invoice 42" https://<your-app-domain>/files
curl https://<your-app-domain>/files      # the file is there
clever restart
curl https://<your-app-domain>/files      # and now?
```

Why? (Think of Session 1: what happens to an instance at each deployment?)

**Step 2 — Add persistent storage: an FS Bucket**

```bash
clever addon create fs-bucket fs-<your-name> --org {{ORG_NAME}}
clever service link-addon fs-<your-name>
clever addon list --org {{ORG_NAME}}       # find the add-on ID of fs-<your-name>
clever addon env <addon-id>                # note the bucket host: bucket-…-fsbucket.<domain>
clever env set CC_FS_BUCKET /uploads:<bucket-host>
clever restart
```

- `/uploads` is relative to the app's folder: it's where the app writes (`UPLOAD_DIR` defaults to `uploads`).
- The host goes without `https://`.
- The folder **must not exist** in the repository (or must be empty), otherwise the mount is ignored.

**Step 3 — Prove it works**

```bash
curl -X POST --data "invoice 43" https://<your-app-domain>/files
clever restart
curl https://<your-app-domain>/files      # still there?
```

Also find the mount line in the deployment log (`clever logs --since 10m --until now`), and your file in the add-on's **File explorer** in the Console.

More details: [`demos/4-fs-bucket/`](demos/4-fs-bucket/).

## Scenario 5 — "Files vanish again" (15 min)

```bash
cd ~/cc-support-<your-name>
cp -R $LAB/demos/5-fs-bucket-config/files/. .
git add -A && git commit -m "v5"
bash $LAB/demos/5-fs-bucket-config/configure.sh   # the team's new configuration
clever deploy
```

Upload a file, restart, list again.

> **Ticket:** *"Since the last release, uploaded files disappear after every deployment again. And the bucket looks empty in the Console. The FS Bucket is broken!"*

Questions and hints: [`demos/5-fs-bucket-config/`](demos/5-fs-bucket-config/).

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

> `clever logs` and `clever accesslogs` **follow the logs live** and never return on their own: add `--until now` to get a snapshot and your prompt back (or stop with Ctrl+C).

| I want to… | Command |
|------------|---------|
| app status / deployment history | `clever status` · `clever activity` |
| logs of one deployment | `clever logs --deployment-id <id> --until now` |
| runtime logs | `clever logs --since 30m --until now [--search <text>]` |
| access logs | `clever accesslogs --since 30m --until now` |
| app / add-on variables | `clever env` · `clever addon env <addon-id>` |
| redeploy / rebuild | `clever restart` · `clever restart --without-cache` |
| list add-ons | `clever addon list --org {{ORG_NAME}}` |
| info for support | `clever diag` |
