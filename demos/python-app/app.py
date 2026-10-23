"""Clever Cloud training: a plain Python (Flask) web app.

Deployed with the classic Python runtime: requirements.txt + CC_PYTHON_MODULE=app:app.
No uv, no build step: the platform installs the dependencies and serves the WSGI app.

Endpoints:
  GET /        -> version and which instance answered
  GET /health  -> 200 OK, used as a health check
  GET /db      -> records a visit in PostgreSQL (needs a linked PostgreSQL add-on)
"""
import os
import platform

import pg8000.native
from flask import Flask, jsonify

VERSION = "v1"  # Lab 1.6: change this value and redeploy

app = Flask(__name__)


def instance_info():
    return {
        "number": os.environ.get("INSTANCE_NUMBER", "local"),
        "id": os.environ.get("INSTANCE_ID", "local"),
        "commit": os.environ.get("COMMIT_ID", os.environ.get("CC_COMMIT_ID", "local")),
    }


@app.get("/")
def index():
    return jsonify(
        message=os.environ.get("GREETING", "Hello from Clever Cloud"),
        version=VERSION,
        instance=instance_info(),
        python=platform.python_version(),
    )


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/db")
def db():
    host = os.environ.get("POSTGRESQL_ADDON_HOST")
    if not host:
        return jsonify(error="No database configured: POSTGRESQL_ADDON_HOST is not set. "
                             "Is a PostgreSQL add-on linked, and was the app restarted?"), 503
    conn = pg8000.native.Connection(
        host=host,
        port=int(os.environ.get("POSTGRESQL_ADDON_PORT", "5432")),
        database=os.environ["POSTGRESQL_ADDON_DB"],
        user=os.environ["POSTGRESQL_ADDON_USER"],
        password=os.environ["POSTGRESQL_ADDON_PASSWORD"],
    )
    try:
        conn.run("""CREATE TABLE IF NOT EXISTS visits (
                      id SERIAL PRIMARY KEY,
                      at TIMESTAMPTZ NOT NULL DEFAULT now(),
                      instance TEXT)""")
        conn.run("INSERT INTO visits (instance) VALUES (:i)", i=instance_info()["number"])
        count, db_time = conn.run("SELECT count(*), now() FROM visits")[0]
        return jsonify(visits=count, db_time=db_time.isoformat(), instance=instance_info()["number"])
    finally:
        conn.close()


if __name__ == "__main__":
    # Local run only. On Clever Cloud, the platform serves `app` through uWSGI (CC_PYTHON_MODULE=app:app).
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
