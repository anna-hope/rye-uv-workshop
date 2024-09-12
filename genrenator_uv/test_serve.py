import pytest

import serve


@pytest.fixture()
def app():
    return serve.app


@pytest.mark.asyncio(loop_scope="session")
async def test_index(app):
    client = app.test_client()
    response = await client.get("/")
    assert await response.data
