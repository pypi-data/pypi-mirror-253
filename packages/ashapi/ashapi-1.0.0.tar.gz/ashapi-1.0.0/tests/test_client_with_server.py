import pytest

from conftest import skip_when_no_server_running, real_server_config

from ashapi.client import SimcomplexClient

import websockets

@skip_when_no_server_running
@pytest.mark.asyncio
async def test_websockets_connect_no_context_manager():
    '''
    This test shows how to properly use websocket (websockets.WebSocketClientProtocol) without context manager.
    One should call await websocket.close() to avoid huge exceptions backlog when after test finishes.
    Comment last string to see the exceptions (when websocket is not properly closed).
    '''

    websocket = await websockets.connect(real_server_config.ws_uri, open_timeout=1.0)

    assert websocket.state == websockets.protocol.OPEN

    await websocket.close()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_websockets_connect_with_context_manager():
    '''
    This test shows how to safely open websocket (websockets.WebSocketClientProtocol) using context manager.
    '''
    async with websockets.connect(real_server_config.ws_uri, open_timeout=1.0) as websocket:
        assert websocket.state == websockets.protocol.OPEN


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_client_connect():

    client = SimcomplexClient(real_server_config)

    await client.connect()

    assert client.connected

    await client.disconnect() # to avoid huge exceptions backlog when after test finishes


from contextlib import asynccontextmanager

@asynccontextmanager
async def client_connected(client):
    await client.connect()
    yield client
    await client.disconnect()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_client_connect_context_manager():

    client = SimcomplexClient(real_server_config)

    async with client_connected(client) as c:
        assert c.connected



