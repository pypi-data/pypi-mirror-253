import pytest
import asyncio

from ashapi.events import EventBus

@pytest.fixture(scope='function')
def ebus():
    return EventBus()


def test_eventbus_construct():

    ebus = EventBus()

    assert ebus.total_listeners == 0
    assert len(ebus["some_custom_event"]) == 0


def test_eventbus_add_listener_and_remove(ebus):

    def handler(payload):
        payload['calls'] = payload['calls'] + 1

    def handler1(payload):
        pass

    ebus.add_listener("custom", handler)

    assert ebus.total_listeners == 1
    assert len(ebus["custom"]) == 1

    ebus.remove_listener("custom", handler)

    assert ebus.total_listeners == 0
    assert len(ebus["custom"]) == 0

    ebus.remove_listener("custom", handler1) # remove unexisting listener

    assert ebus.total_listeners == 0
    assert len(ebus["custom"]) == 0

    payload = {'calls': 0}

    ebus.emit("custom", payload) # does nothing

    assert ebus.total_listeners == 0
    assert len(ebus["custom"]) == 0



def test_eventbus_add_listener_and_emit(ebus):

    def handler(payload):
        payload['calls'] = payload['calls'] + 1

    ebus.add_listener("custom", handler)

    assert ebus.total_listeners == 1
    assert len(ebus.listeners["custom"]) == 1

    payload = {'calls': 0}

    ebus.emit("custom", payload)

    assert payload['calls'] == 1

    ebus.emit("custom", payload)

    assert payload['calls'] == 2

    assert ebus.total_listeners == 1
    assert len(ebus.listeners["custom"]) == 1


def test_eventbus_add_unique_listeners(ebus):

    def handler(payload):
        payload['calls'] = payload['calls'] + 1

    ebus.add_listener("custom", handler)
    ebus.add_listener("custom", handler)

    assert ebus.total_listeners == 1
    assert len(ebus["custom"]) == 1


def test_eventbus_add_two_listeners_and_emit(ebus):

    def handler1(payload):
        payload['calls1'] = payload['calls1'] + 1

    def handler2(payload):
        payload['calls2'] = payload['calls2'] + 1

    ebus.add_listener("custom1", handler1)
    ebus.add_listener("custom2", handler2)

    assert ebus.total_listeners == 2
    assert len(ebus["custom1"]) == 1
    assert len(ebus["custom2"]) == 1

    payload = {'calls1': 0, 'calls2': 0}

    ebus.emit("custom1", payload)
    ebus.emit("custom1", payload)
    ebus.emit("custom2", payload)

    assert payload['calls1'] == 2
    assert payload['calls2'] == 1

    assert ebus.total_listeners == 2
    assert len(ebus["custom1"]) == 1
    assert len(ebus["custom2"]) == 1


@pytest.mark.asyncio
async def test_eventbus_add_listener_and_emit_async(ebus):

    async def handler(payload):
        await asyncio.sleep(0.2)
        payload['calls'] = payload['calls'] + 1

    ebus.add_listener("custom", handler)

    assert ebus.total_listeners == 1
    assert len(ebus.listeners["custom"]) == 1

    payload = {'calls': 0}

    await ebus.emit_async("custom", payload)

    assert payload['calls'] == 1

    await ebus.emit_async("custom", payload)

    assert payload['calls'] == 2

    assert ebus.total_listeners == 1
    assert len(ebus.listeners["custom"]) == 1


@pytest.mark.asyncio
async def test_eventbus_add_mix_listener_and_emit_async(ebus):

    def handler(payload):
        payload['calls'] = payload['calls'] + 1

    async def handler_async(payload):
        await asyncio.sleep(0.2)
        payload['calls_async'] = payload['calls_async'] + 1

    ebus.add_listener("custom", handler)
    ebus.add_listener("custom", handler_async)

    assert ebus.total_listeners == 2
    assert len(ebus.listeners["custom"]) == 2

    payload = {'calls': 0, 'calls_async': 0}

    await ebus.emit_async("custom", payload)

    assert payload['calls'] == 1
    assert payload['calls_async'] == 1

    await ebus.emit_async("custom", payload)

    assert payload['calls'] == 2
    assert payload['calls_async'] == 2

    assert ebus.total_listeners == 2
    assert len(ebus.listeners["custom"]) == 2


@pytest.mark.asyncio
async def test_eventbus_add_mix_listener_and_emit(ebus):

    def handler(payload):
        payload['calls'] = payload['calls'] + 1

    async def handler_async(payload):
        await asyncio.sleep(0.2)
        payload['calls_async'] = payload['calls_async'] + 1

    ebus.add_listener("custom", handler)
    ebus.add_listener("custom", handler_async)

    assert ebus.total_listeners == 2
    assert len(ebus.listeners["custom"]) == 2

    payload = {'calls': 0, 'calls_async': 0}

    ebus.emit("custom", payload)

    await asyncio.sleep(0.3) # really strange, sleeping less than 0.3 doesn't succeed in calling scheduled handler_async ...

    assert payload['calls'] == 1
    assert payload['calls_async'] == 1

    ebus.emit("custom", payload)

    await asyncio.sleep(0.3) # really strange, sleeping less than 0.3 doesn't succeed in calling scheduled handler_async ...

    assert payload['calls'] == 2
    assert payload['calls_async'] == 2

    assert ebus.total_listeners == 2
    assert len(ebus.listeners["custom"]) == 2
