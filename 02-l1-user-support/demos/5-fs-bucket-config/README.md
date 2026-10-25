# Scenario 5 — "Files vanish again"

> **Ticket:** *"Since the last release, uploaded files disappear after every deployment again. And the bucket looks empty in the Console. The FS Bucket is broken!"*

Apply the overlay, then the team's new configuration, then deploy (from your app folder):

```bash
cp -R <session-folder>/demos/5-fs-bucket-config/files/. .
git add -A && git commit -m "release 5"
bash <session-folder>/demos/5-fs-bucket-config/configure.sh
clever deploy
```

Upload a file, restart, list again. Then investigate:

1. Is the FS Bucket broken? How can you tell (Console, deployment log)?
2. Is the bucket mounted? Where is the app writing? (`GET /files` tells you its `upload_dir`.)
3. What changed in this release — in the code *and* in the configuration?
4. There is more than one problem. Find them all, fix them, prove it works.
