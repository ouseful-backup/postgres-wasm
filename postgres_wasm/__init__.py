"""
Return config on servers to start for postgres_wasm
See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""

import os
import importlib.resources


def setup_postgres_wasm():
    with importlib.resources.path("postgres_wasm", "static") as fpath:
        command = ["python3", "-m", "http.server", "--directory", str(fpath), "{port}"]
        icon_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "icons", "postgresql.svg"
        )
        return {
            "command": command,
            "environment": {},
            "launcher_entry": {"title": "postgres_wasm", "icon_path": icon_path},
        }
