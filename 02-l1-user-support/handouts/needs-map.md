# Needs map — "I need…" → what the platform offers

People ask for a **solution** they know. Ask *"what do you want to achieve?"*, then map the **need**.

| The user asks for… | Ask | The need is often… | The platform answer |
|--------------------|-----|--------------------|---------------------|
| "A server / a VM" | What will run on it? | Running an app, an API, a worker | An **application** (Python, Node.js, Java, Go, PHP, Docker…) |
| "A VM with root access" | What do you need to install? | A system package (ImageMagick, a font, a binary) | A **Docker** application (the Dockerfile brings the packages), or the runtime's build options |
| "A database" | Which engine? For which app(s) and environment? How critical is the data? | Persistent data | An **add-on** (PostgreSQL, MySQL, MongoDB, Redis…), one per environment, linked to the app |
| "To store files" | What kind, how big, who reads them? | User uploads, generated documents, backups | **Cellar** (S3-compatible object storage); an **FS Bucket** only for apps that need a file system |
| "A job every night" | How long does it run? On every instance? | A scheduled task | **CRON** (`clevercloud/cron.json`, UTC times, runs on every instance) — not available for Docker apps |
| "To run a script once" | Is it a migration? Does it need the app's environment? | A one-off task | A **task** application (`clever create --task`, or `CC_TASK=true`), or `clever ssh` for a one-time intervention |
| "A Kubernetes cluster" | What will you deploy? Who operates it? | Running containers / existing manifests | A **namespace** in the shared CKE cluster (platform team) — or simply an application if it's a single web app |
| "More power" | What is slow? Since when? | CPU/RAM, more instances, or a bug | **Scaling** (flavor, number of instances, autoscaling bounds) — after checking it's not a bug or a dependency |
| "Access to the database from my laptop" | What for? Read or write? Which environment? | Debugging, a migration, a BI tool | The add-on's connection information — **within your security policy**; never production credentials on a laptop by default |
| "A new environment" | Same as which one? | staging, a test copy | A new **app + add-ons** with the same configuration (scripts, Terraform) — in the right organisation |

When the answer is **"not possible here"**: say it clearly, say why, and propose the closest option or route the request (platform team, architecture review).
