# Session 1 — Lab: an app, a database, a Kubernetes cluster

*Hands-on guide for trainees. Replace `<your-name>` by your first name (lowercase, no spaces) so that everyone's resources are easy to tell apart.*

## Your platform

| Parameter | Value |
|-----------|-------|
| Console | `{{CONSOLE_URL}}` |
| Organisation | `{{ORG_NAME}}` |
| Zone (region) | `{{ZONE}}` |
| Application domain | `{{APP_DOMAIN}}` |
| Training CKE cluster | `{{CLUSTER_NAME}}` (created by the trainer during the session) |

> Clever Tools commands that manage an application assume you are in the app folder: it is linked to your application through the `.clever.json` file created by `clever create`.

---

## Lab 0 — Check your setup (2 min)

```bash
clever profile                         # your account, the right API host
clever applications list --org {{ORG_NAME}}
kubectl version --client
```

Open the Console in your browser and select the organisation `{{ORG_NAME}}`.

---

## Lab 1 — A plain Python app (25 min)

### 1.1 Get the app and make it a Git repository

```bash
cp -r <session-folder>/demos/python-app ~/cc-python-<your-name>
cd ~/cc-python-<your-name>
git init
git add .
git commit -m "Initial commit"
```

Look at the three files (2 min): `app.py` is a small Flask app, `requirements.txt` lists its dependencies. There is no server configuration, no Dockerfile, no build script.

### 1.2 Create the application

```bash
clever create --type python --org {{ORG_NAME}} --region {{ZONE}} python-<your-name>
cat .clever.json
clever status
```

👉 In the Console, open your application and look around: **Information** (app ID, deployment URL), **Environment variables**, **Scalability**, **Domain names**, **Logs**, **Metrics**, **Activity**.

### 1.3 Tell the platform what to run

The Python runtime serves a WSGI app. It needs to know which one: module `app` (the file `app.py`), object `app` (the Flask instance).

```bash
clever env set CC_PYTHON_MODULE app:app
clever env set CC_PYTHON_VERSION 3.13
clever env
```

### 1.4 Deploy and read the deployment log

```bash
clever deploy
```

While it runs, spot these steps in the log and note the line you see for each:

- [ ] the commit being deployed
- [ ] the Python version chosen
- [ ] the dependency installation from `requirements.txt`
- [ ] the build cache being created/uploaded
- [ ] the check that something listens on port 8080
- [ ] the deployment success

### 1.5 Test and observe

```bash
clever domain                    # the app's domain
curl https://<your-app-domain>/
clever activity                  # deployment history
clever instances                 # running instances
clever logs --since 10m          # application logs (Ctrl+C to stop)
clever accesslogs --since 10m    # HTTP access logs
```

Which `instance.number` answered? Which `commit`?

### 1.6 A new version, without downtime

In a **second terminal**, poll the app every second:

```bash
while true; do curl -s https://<your-app-domain>/ | grep -o '"version":"[^"]*"'; sleep 1; done
```

In `app.py`, change `VERSION = "v1"` to `"v2"`, then:

```bash
git commit -am "v2"
clever deploy
```

Watch the polling terminal: does it ever fail? When does the version switch? Why?

---

## Lab 2 — Add-ons (20 min)

### 2.1 What's available?

```bash
clever addon providers
clever addon providers show postgresql-addon      # plans and zones
```

👉 Console: organisation → **Create** → **an add-on**: browse the catalogue.

### 2.2 Before linking

```bash
curl https://<your-app-domain>/db
```

What does it answer? Why?

### 2.3 Create and link a PostgreSQL add-on

```bash
clever addon create postgresql-addon pg-<your-name> --plan dev --region {{ZONE}} --org {{ORG_NAME}}
clever service link-addon pg-<your-name>
```

*(Console alternative: create the add-on, then in the app → **Service dependencies** → link it.)*

### 2.4 What did linking change?

```bash
clever addon list --org {{ORG_NAME}}
clever addon env <addon-id>          # the add-on's variables
clever env                           # the app's variables: what do you see?
curl https://<your-app-domain>/db    # still 503?
```

The add-on's variables (`POSTGRESQL_ADDON_HOST`, `…_USER`, `…_PASSWORD`…) are **injected into the application's environment when it starts**. A running instance doesn't see them yet.

```bash
clever restart
curl https://<your-app-domain>/db    # call it several times
```

👉 Console: open the add-on — dashboard, connection information, **Backups**, **Metrics**.

---

## Lab 3 — A modern Python app with uv (trainer demo, 10 min)

The trainer deploys the [Django todo-list example](https://github.com/CleverCloud/django-todo-list-example) (uv + PostgreSQL; snapshot in `demos/django-todo-uv/`). Watch and answer:

1. Which file tells the platform to use **uv** instead of the classic mode? Which environment variable is also required?
2. `CC_PYTHON_MODULE` is not set. Why isn't it needed here?
3. Where do the database credentials come from? Compare with Lab 2.
4. The migrations run in `CC_PRE_RUN_HOOK`. What could go wrong with 3 instances?
5. If a developer opens a ticket "my uv app deploys but answers *Bad Request (400)*", what would you check? (Hint: `ALLOWED_HOSTS`.)

---

## Lab 4 — Clever Kubernetes Engine (30 min)

### 4.1 Watch the cluster creation (trainer demo)

In real life, developers don't create clusters: the platform team runs one or two **shared clusters** per organisation, and each team gets a namespace. That's exactly the setup of this lab. The trainer plays the platform team, shows the options and creates the training cluster:

```bash
clever k8s create {{CLUSTER_NAME}} --org {{ORG_NAME}} --watch
```

Note the options available: `--topology` (`ALL_IN_ONE`, `DEDICATED_COMPUTE`, `DISTRIBUTED`), `--flavor`, `--replication-factor`, `--cluster-version`, `--nodegroup`, `--autoscaling`, `--persistent-storage`. Topology and replication factor can't be changed after creation.

### 4.2 Get your kubeconfig

```bash
clever k8s list --org {{ORG_NAME}}
clever k8s get {{CLUSTER_NAME}} --org {{ORG_NAME}}
mkdir -p ~/.kube
clever k8s get-kubeconfig {{CLUSTER_NAME}} --org {{ORG_NAME}} > ~/.kube/cc-training.yaml
export KUBECONFIG=~/.kube/cc-training.yaml        # don't overwrite your existing ~/.kube/config
kubectl get nodes
```

> ⚠️ This kubeconfig gives full access to the cluster. Treat it as a secret.

### 4.3 Your own namespace and workload

```bash
kubectl create namespace <your-name>
kubectl apply -n <your-name> -f <session-folder>/demos/k8s/whoami.yaml
kubectl get deploy,pods,svc -n <your-name> -o wide
```

### 4.4 Reach it

```bash
kubectl port-forward -n <your-name> svc/whoami 8081:80
# in another terminal:
curl http://localhost:8081/
```

Which pod answered? Call it several times.

### 4.5 Logs, events, self-healing

```bash
kubectl logs -n <your-name> deploy/whoami
kubectl get events -n <your-name> --sort-by=.lastTimestamp
kubectl delete pod -n <your-name> <one-of-the-pod-names>
kubectl get pods -n <your-name> -w        # Ctrl+C when a new pod is Running
```

What happened? Who recreated the pod: Kubernetes or Clever Cloud?

### 4.6 (Optional) Scale

```bash
kubectl scale -n <your-name> deploy/whoami --replicas=4
kubectl get pods -n <your-name> -o wide
```

### 4.7 Public exposure (trainer demo)

The trainer exposes a service through a CKE `LoadBalancer` (quota: one per organisation by default) and shows the public IPs it gets.

---

## Lab 5 — Clean up (2 min)

*Unless the trainer asks you to keep your resources for the next sessions.*

```bash
kubectl delete namespace <your-name>
unset KUBECONFIG
cd ~/cc-python-<your-name>
clever service unlink-addon pg-<your-name>
clever addon delete pg-<your-name> --org {{ORG_NAME}}
clever delete
```

---

## Cheat sheet

| I want to… | Command | Console |
|------------|---------|---------|
| create an app | `clever create --type python <name>` | Create → an application |
| link a folder to an existing app | `clever link <app-id\|name>` | — |
| deploy | `clever deploy` | — |
| status / history / instances | `clever status` / `clever activity` / `clever instances` | Overview / Activity |
| logs / access logs | `clever logs [--since 1h] [--search txt]` / `clever accesslogs` | Logs |
| env vars | `clever env`, `clever env set K V`, `clever env rm K` | Environment variables |
| restart / rebuild / roll back | `clever restart [--without-cache] [--commit <id>]` | Overview / Activity |
| scale | `clever scale --flavor S --instances 2` | Scalability |
| add-on catalogue | `clever addon providers [show <provider>]` | Create → an add-on |
| create / link an add-on | `clever addon create …` / `clever service link-addon …` | Service dependencies |
| add-on variables | `clever addon env <addon-id>` | Add-on → Information |
| list / inspect clusters | `clever k8s list` / `clever k8s get <cluster>` | — |
| kubeconfig | `clever k8s get-kubeconfig <cluster> > file` | — |
| cluster events / quota | `clever k8s activity <cluster>` / `clever k8s quota` | — |
| node groups | `clever k8s nodegroups list <cluster>` | — |
| collect info for support | `clever diag` | — |

Docs: <https://www.clever.cloud/developers/doc/> · CLI reference: <https://www.clever.cloud/developers/doc/cli-reference/> · CKE: <https://www.clever.cloud/developers/doc/deploy/kubernetes/>
