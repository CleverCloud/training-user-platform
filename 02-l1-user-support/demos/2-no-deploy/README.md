# Scenario 2 — "My change isn't online"

> **Ticket:** *"I pushed version 2 of the app an hour ago and it still shows version 1! Is the platform down?"*

Apply the overlay and deploy (see [`../README.md`](../README.md)), then answer:

1. Qualify the ticket: what, where, since when, what changed? Which identifiers do you need?
2. Is the platform down? Is the app down? What does `curl https://<your-app-domain>/` answer?
3. Where is the explanation? (`clever activity`, the deployment logs in the Console, `clever logs --deployment-id <id>`)
4. Why does the app still answer?
5. What do you tell the developer, and how do they fix it?
