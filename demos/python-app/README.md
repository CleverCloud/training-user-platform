# Plain Python app — Clever Cloud user training

A minimal Flask app deployed with the **classic Python runtime**: a `requirements.txt`, no build step, no uv.
The platform installs the dependencies and serves the app (uWSGI behind Nginx).

| Endpoint | What it shows |
|----------|---------------|
| `GET /` | version, instance number/id, commit, Python version |
| `GET /health` | health check target |
| `GET /db` | add-on linking: reads the `POSTGRESQL_ADDON_*` variables injected by a linked PostgreSQL add-on |

Required on Clever Cloud: `CC_PYTHON_MODULE=app:app` (module `app.py`, Flask object `app`).

The PostgreSQL driver is `pg8000`, a pure-Python driver: nothing to compile.

Run locally (optional): `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt && .venv/bin/python app.py`, then `curl localhost:8080`.
