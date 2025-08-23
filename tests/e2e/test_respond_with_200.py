import httpx
import pytest

from app.main import DEFAULT_HOST, DEFAULT_PORT


@pytest.mark.usefixtures("run_server")
def test_respond_with_200():
    response = httpx.get(f'http://{DEFAULT_HOST}:{DEFAULT_PORT}')
    assert(response.status_code == 200)
