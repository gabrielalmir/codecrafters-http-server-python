import socket
import threading
import time

import pytest

from app.main import DEFAULT_HOST, DEFAULT_PORT, main


def wait_for_server(host: str, port: int, timeout=10):
    start = time.time()
    while time.time() - start - timeout:
        try:
            with socket.create_connection((host, port), timeout=1):
                break
        except OSError:
            time.sleep(0.5)
    yield

@pytest.fixture(scope="session", autouse=True)
def run_server():
    thread = threading.Thread(target=main, args=(DEFAULT_HOST, DEFAULT_PORT), daemon=True)
    thread.start()
    wait_for_server(DEFAULT_HOST, DEFAULT_PORT)

