import pytest
import pytest_asyncio

from conftest import skip_when_server_running

from ashapi.config import Config
from ashapi.client import SimcomplexClient
from ashapi.events import Events


@pytest_asyncio.fixture(scope='function')
async def with_client():
    config = Config.localhost()
    client = SimcomplexClient(config)
    yield client
    await client.disconnect()


@skip_when_server_running
@pytest.mark.asyncio
async def test_client_no_connection(with_client):

    client = with_client

    await client.connect()

    assert not client.connected



@skip_when_server_running
@pytest.mark.asyncio
async def test_client_no_connection_autoconnect(with_client):

    client = with_client
    client.config.autoreconnect = True

    num_connection_refused = 0

    def on_connection_refused(data=None):
        nonlocal num_connection_refused
        num_connection_refused += 1
        if num_connection_refused == 3:
            client.unsubscribe(Events.CONNECTION_REFUSED, on_connection_refused)
            client.config.autoreconnect = False

    client.subscribe(Events.CONNECTION_REFUSED, on_connection_refused)

    await client.connect()

    await client.run(duration=4)

    assert num_connection_refused == 3
    assert not client.connected
