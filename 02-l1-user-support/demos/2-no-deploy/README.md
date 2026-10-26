# Scenario 2 — "My change isn't online"

> **Ticket:** *"I pushed version 2 of the app an hour ago and it still shows version 1! Is the platform down?"*

Apply the release and deploy:

```bash
cd ~/cc-support-<your-name>
cp -R $LAB/demos/2-no-deploy/files/. .
git add -A && git commit -m "v2"
clever deploy
```

Then answer:

1. Qualify the ticket: what, where, since when, what changed? Which identifiers do you need?
2. Is the platform down? Is the app down? What does `curl https://<your-app-domain>/` answer?
3. Where is the explanation? (`clever activity`, the deployment logs in the Console, `clever logs --deployment-id <id> --until now`)
4. Why does the app still answer?
5. What do you tell the developer, and how do they fix it?
