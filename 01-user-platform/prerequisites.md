# Session 1 — Using the Clever Cloud platform: prerequisites

*To forward to the customer contact. Everything below should be ready **before the session**, and ideally checked the day before: the session is hands-on from the first minutes, and every setup issue fixed during the session costs time for the whole group.*

## 1. On the platform (to be prepared by the platform team)

| # | What | Why |
|---|------|-----|
| 1.1 | **One training organisation** (e.g. `training-support`) on the platform used by your developers | Isolated sandbox; can be deleted after the program |
| 1.2 | **One account per trainee** (and one for the trainer), each a member of that organisation with the **Admin** or **Manager** role | Trainees create/delete applications and add-ons |
| 1.3 | Enough **quota/credit** in that organisation for, per trainee: 1 Python application (small flavor) + 1 PostgreSQL add-on (smallest plan) | Labs 1 and 2 |
| 1.4 | **Python** runtime and **PostgreSQL** add-on available | Labs 1 and 2 |
| 1.5 | **Clever Kubernetes Engine (CKE)** available to the organisation, with quota for **one** small cluster (default `ALL_IN_ONE` topology, flavor `S`: 8 vCPU / 12 GB) and **one** `LoadBalancer` service | Lab 4 (one shared cluster created by the trainer) |
| 1.6 | **Kubernetes feature enabled for every account** (CKE is in beta: Console → Labs, or `clever features enable k8s`) | Lab 4 |
| 1.7 | Metrics/Grafana and log access enabled for the organisation, if available on your installation | Observability |

## 2. Information we need from you

Please send back the following values (they will be used in the lab instructions):

| Parameter | Public Clever Cloud value (for reference) | Your value |
|-----------|-------------------------------------------|------------|
| Console URL | `https://console.clever-cloud.com` | |
| API host | `https://api.clever-cloud.com` | |
| Auth bridge host | `https://api-bridge.clever-cloud.com` | |
| SSH gateway | `ssh@sshgateway-clevercloud-customers.services.clever-cloud.com` | |
| Default application domain | `*.cleverapps.io` | |
| Zone (region) name to use | `par` | |
| Name of the training organisation | — | |
| List of add-ons available on your installation | see `clever addon providers` | |
| OAuth consumer key/secret for Clever Tools (only if your installation requires custom ones) | built in | |
| Corporate HTTP proxy / custom CA certificate (if any) | — | |
| Number of trainees and their usual role (developer, ops, helpdesk…) | — | |

## 3. On each trainee's workstation

| # | What | How to check |
|---|------|--------------|
| 3.1 | **Git** ≥ 2.x, with `user.name` and `user.email` configured | `git --version`, `git config user.email` |
| 3.2 | **Clever Tools** (CLI), version **4.9 or later** (5.x recommended) | `clever version` |
| 3.3 | **Logged in** with Clever Tools to the platform above (see below) | `clever profile` shows the trainee's account |
| 3.4 | **kubectl** (any version within one minor of Kubernetes 1.34–1.36) | `kubectl version --client` |
| 3.5 | A web browser able to reach the Console and the application domain | Open the Console URL and log in |
| 3.6 | A terminal and a code editor; `curl` | `curl --version` |
| 3.7 | *Optional:* Python ≥ 3.10 to run the demo app locally | `python3 --version` |
| 3.8 | Network: HTTPS access to the Console, API, auth bridge, Git endpoint and application domain; HTTPS access to the Kubernetes API endpoint of CKE clusters | `clever profile` and `clever applications list` both work |

Installation guides:
- Clever Tools: <https://www.clever.cloud/developers/doc/manage/cli/install> (binaries for Linux/macOS/Windows, packages, or `npm install -g clever-tools`)
- kubectl: <https://kubernetes.io/docs/tasks/tools/#kubectl>

### Logging in to a non-default platform

On the public Clever Cloud, `clever login` is enough. On a dedicated or on-premises installation, the CLI must be pointed at your endpoints once (the values from section 2):

```bash
clever login \
  --api-host <API host> \
  --console-url <Console URL> \
  --auth-bridge-host <Auth bridge host> \
  --ssh-gateway <SSH gateway>
  # add --oauth-consumer-key / --oauth-consumer-secret only if required
```

The overrides are stored in the CLI profile, so this is done only once.

### Behind a corporate proxy or with a private CA

- Proxy: export `https_proxy` / `http_proxy` (and `no_proxy`) in the shell; Git follows `git config --global http.proxy` or the same variables.
- Private CA: install it in the OS certificate store (recommended), or export `NODE_EXTRA_CA_CERTS=/path/to/ca.pem` for the CLI and `git config --global http.sslCAInfo /path/to/ca.pem` for Git.
- Never disable TLS verification.

Reference: <https://www.clever.cloud/developers/doc/manage/cli/>

## 4. Quick self-check (5 minutes, the day before)

Each trainee runs:

```bash
git --version
clever version                       # 4.9 or later
clever profile                       # your account, the right API host
clever applications list             # no error (an empty list is fine)
clever features enable k8s           # once
clever k8s list --org <training org> # no error (an empty list is fine)
kubectl version --client
```

…and logs into the Console in a browser. If any of these fail, please tell us before the session.
