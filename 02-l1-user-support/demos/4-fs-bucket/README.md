# Scenario 4 — "My files disappear": add an FS Bucket

The app can store files (`POST /files`) and list them (`GET /files`).

## Step 1 — See the problem

Apply the overlay and deploy, then:

```bash
curl -X POST --data "invoice 42" https://<your-app-domain>/files
curl https://<your-app-domain>/files      # the file is there
clever restart
curl https://<your-app-domain>/files      # and now?
```

Why? (Think of Session 1: what happens to an instance at each deployment?)

## Step 2 — Add persistent storage

An **FS Bucket** is a network file system, mounted into the application's folder at start.

```bash
clever addon create fs-bucket fs-<your-name> --org {{ORG_NAME}} --region {{ZONE}}
clever service link-addon fs-<your-name>
clever addon env <addon-id>         # note the bucket host: bucket-…-fsbucket.<domain>
clever env set CC_FS_BUCKET /uploads:<bucket-host>
clever restart
```

- `/uploads` is relative to the app's folder (`$APP_HOME/uploads`): it's where the app writes (`UPLOAD_DIR` defaults to `uploads`).
- The folder **must not exist** in the repository (or must be empty), otherwise the mount is ignored.

## Step 3 — Check it works

1. Find the mount line in the deployment log.
2. Upload a file, restart, list again: is it still there?
3. Open the add-on in the Console: find your file in the **File explorer**.

Docs: <https://www.clever.cloud/developers/doc/deploy/storage/fs-bucket/>
