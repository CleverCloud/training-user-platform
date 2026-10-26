# Scenario 3 — "It works, then it errors"

> **Ticket:** *"Since this morning's release, `/db` works for a few calls, then only returns errors. Restarting the app fixes it for a minute. Is the database broken?"*

Apply the release, deploy, then call `/db` about ten times:

```bash
cd ~/cc-support-<your-name>
cp -R $LAB/demos/3-connections/files/. .
git add -A && git commit -m "v3"
clever deploy
for i in $(seq 1 10); do curl -s -o /dev/null -w "%{http_code}\n" https://<your-app-domain>/db; done
```

Answer:

1. Did the deployment succeed? Does the deployment log help this time?
2. Where is the error? (`clever logs --since 10m --until now`, the Console's logs)
3. What exactly does the error say? Who says it: the app, or the database?
4. Which plan is the PostgreSQL add-on on, and what are its limits?
5. Why does a restart "fix" it for a minute?
6. What are the possible fixes — on the app side, on the add-on side? Which would you recommend?
