# Lab apps

One application, deployed once, then changed scenario after scenario — exactly like a developer's app over a few weeks.

| Folder | Scenario | What you do |
|--------|----------|-------------|
| [`1-base/`](1-base/) | The normal case | Copy it, make it a Git repo, create the app and its PostgreSQL add-on, deploy |
| [`2-no-deploy/`](2-no-deploy/) | Ticket: "my change isn't online" | Apply the overlay, deploy, investigate |
| [`3-connections/`](3-connections/) | Ticket: "it works, then errors" | Apply the overlay, deploy, call `/db` a few times, investigate |
| [`4-fs-bucket/`](4-fs-bucket/) | "My files disappear": add an FS Bucket | Apply the overlay, see the problem, configure an FS Bucket |
| [`5-fs-bucket-config/`](5-fs-bucket-config/) | Ticket: "files vanish again" | Apply the overlay and the team's configuration, deploy, investigate |

**Applying an overlay** (from your app folder; `$LAB` is this session's folder, see `lab.md`):

```bash
cd ~/cc-support-<your-name>
cp -R $LAB/demos/<scenario>/files/. .
git add -A && git commit -m "<scenario>"
clever deploy
```

Start each investigation from the **ticket and the logs**, not from the diff: in real life you rarely get the diff.
