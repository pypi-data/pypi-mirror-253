import pytest
import pytest_asyncio
import asyncio

import json

from conftest import skip_when_no_server_running, real_server_config

from ashapi.simrequests import (
    SceneClear as RequestSceneClear,
    SceneNew as RequestSceneNew,
    SceneOpen as RequestSceneOpen,
    RecordingOpen as RequestRecordingOpen
)

from ashapi.client import SimcomplexClient
from ashapi.simulation import Simulation


@pytest_asyncio.fixture(scope='function')
async def client():
    '''Arrange client connected to server'''
    client = SimcomplexClient(real_server_config)
    await client.connect()
    asyncio.create_task(client.run())
    print("client prepared")
    yield client
    await client.disconnect()


async def clear_scene(client):
    '''Clear scene prior running test'''
    client.send_request(RequestSceneClear())
    client.send_request(RequestSceneNew())
    await asyncio.sleep(0.1)


async def load_scene(client, path, delay=0.1):
    '''Load scene prior running test'''
    client.send_request(RequestSceneClear())
    client.send_request(RequestSceneOpen(path))
    await asyncio.sleep(delay)


async def load_recording(client, path, delay=0.1):
    '''Load recording prior running test'''
    client.send_request(RequestSceneClear())
    client.send_request(RequestRecordingOpen(path))
    await asyncio.sleep(delay)



@skip_when_no_server_running
@pytest.mark.asyncio
async def test_simulation_after_connect(client):

    sim = Simulation()._attach(client)

    await clear_scene(client)

    assert not sim.is_running
    assert sim.is_paused
    assert sim.is_recording
    assert not sim.is_playback

    assert sim.time == 0.0
    assert sim.time_zero == 0.0
    assert sim.time_total == 0.0
    assert sim.ticks == 0.0

    assert sim.accel == 1.0
    assert sim.time_ratio == 1
    assert not sim.is_maxaccel

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_recording_after_connect(client):

    sim = Simulation()._attach(client)

    await load_recording(client, 'api/recordings/misv01_accelerating_01.strec')

    assert not sim.is_running
    assert sim.is_paused
    assert sim.is_recording
    assert sim.is_playback

    assert sim.time == 0.0
    assert sim.time_zero == 0.0
    assert sim.time_total == 0.0
    assert sim.ticks == 0.0

    assert sim.accel == 1.0
    assert sim.time_ratio == 1
    assert not sim.is_maxaccel

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_simulation_run(client):

    sim = Simulation()._attach(client)

    await clear_scene(client)

    run_simulation_response = ""
    def on_run_simulation(response_text):
        nonlocal run_simulation_response
        js = json.loads(response_text)
        run_simulation_response = js['message']

    sim.run(on_run_simulation)

    # await client.run(duration=0.5)
    await asyncio.sleep(0.5)

    assert sim.is_running
    assert not sim.is_paused
    assert sim.is_recording
    assert not sim.is_playback

    assert sim.time >= 0.4
    assert sim.time_zero == 0.0
    assert sim.accel == 1.0
    assert sim.time_ratio == 1
    assert not sim.is_maxaccel

    assert run_simulation_response == "simulation is running"

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_recording_run(client):

    sim = Simulation()._attach(client)

    await load_recording(client, 'api/recordings/misv01_accelerating_01.strec')

    run_simulation_response = ""
    def on_run_simulation(response_text):
        nonlocal run_simulation_response
        js = json.loads(response_text)
        run_simulation_response = js['message']

    sim.run(on_run_simulation)

    # await client.run(duration=0.5)
    await asyncio.sleep(0.5)

    assert sim.is_running
    assert not sim.is_paused
    assert sim.is_recording
    assert sim.is_playback

    assert sim.time >= 0.4
    assert sim.time_zero == 0.0
    assert sim.accel == 1.0
    assert sim.time_ratio == 1
    assert not sim.is_maxaccel

    assert run_simulation_response == "simulation is running"

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_simulation_run_with_accel(client):

    sim = Simulation()._attach(client)

    await clear_scene(client)

    run_simulation_response = ""
    def on_run_simulation(response_text):
        nonlocal run_simulation_response
        js = json.loads(response_text)
        run_simulation_response = js['message']

    accel_simulation_response = ""
    def on_accel_simulation(response_text):
        nonlocal accel_simulation_response
        js = json.loads(response_text)
        accel_simulation_response = js['message']

    sim.run(on_run_simulation)

    sim.setaccel(10.0, on_accel_simulation) # 10x

    # await client.run(duration=0.5)
    await asyncio.sleep(0.5)

    assert sim.is_running
    assert not sim.is_paused
    assert sim.is_recording
    assert not sim.is_playback

    assert sim.time >= 3.0
    assert sim.time_zero == 0.0
    assert sim.accel == 10.0
    assert sim.time_ratio == 10
    assert not sim.is_maxaccel

    assert run_simulation_response == "simulation is running"
    assert accel_simulation_response == "simulation is running in 10 times faster"

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_simulation_run_with_maxaccel(client):

    sim = Simulation()._attach(client)

    await clear_scene(client)

    run_simulation_response = ""
    def on_run_simulation(response_text):
        nonlocal run_simulation_response
        js = json.loads(response_text)
        run_simulation_response = js['message']

    accel_simulation_response = ""
    def on_accel_simulation(response_text):
        nonlocal accel_simulation_response
        js = json.loads(response_text)
        accel_simulation_response = js['message']

    sim.run(on_run_simulation)

    sim.maxaccel(on_accel_simulation)

    # await client.run(duration=0.5)
    await asyncio.sleep(0.5)

    assert sim.is_running
    assert not sim.is_paused
    assert sim.is_recording
    assert not sim.is_playback

    assert sim.time >= 2.0
    assert sim.time_zero == 0.0
    assert sim.accel == 1.0
    assert sim.time_ratio >= 10
    assert sim.is_maxaccel

    assert run_simulation_response == "simulation is running"
    assert accel_simulation_response == "simulation is running with max possible speed"

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_simulation_pause(client):

    sim = Simulation()._attach(client)

    await clear_scene(client)

    pause_simulation_response = ""
    def on_pause_simuation(response_text):
        nonlocal pause_simulation_response
        js = json.loads(response_text)
        pause_simulation_response = js['message']

    sim.pause(on_pause_simuation)

    await asyncio.sleep(0.1)

    assert not sim.is_running
    assert sim.is_paused
    assert sim.is_recording
    assert not sim.is_playback

    assert sim.time == 0.0
    assert sim.time_zero == 0.0
    assert sim.accel == 1.0
    assert sim.time_ratio == 1
    assert not sim.is_maxaccel

    assert pause_simulation_response == "simulation is paused"

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_simulation_run_until_2nd_sec(client):

    sim = Simulation()._attach(client)

    await clear_scene(client)

    sim.run_until(2)

    # await client.run(duration=2.5)
    await asyncio.sleep(2.5)

    assert sim.time == pytest.approx(2, abs=0.041)
    assert sim.is_paused

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_simulation_run_for_1_sec(client):

    sim = Simulation()._attach(client)

    await clear_scene(client)

    sim.run_for(1)

    # await client.run(duration=1.5)
    await asyncio.sleep(1.5)

    assert sim.time == pytest.approx(1, abs=0.041)
    assert sim.is_paused

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_simulation_step(client):

    sim = Simulation()._attach(client)

    await clear_scene(client)

    run_simulation_response = ""
    def on_run_simulation(response_text):
        nonlocal run_simulation_response
        js = json.loads(response_text)
        run_simulation_response = js['message']

    sim.step(on_run_simulation)

    # await client.run(duration=0.1)
    await asyncio.sleep(0.1)

    assert not sim.is_running
    assert sim.is_paused
    assert sim.is_recording
    assert not sim.is_playback

    assert sim.time == pytest.approx(0.04)
    assert sim.ticks == 1
    assert sim.time_zero == 0.0
    assert sim.accel == 1.0
    assert sim.time_ratio == 1
    assert not sim.is_maxaccel

    assert run_simulation_response == "simulation step is made"

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_simulation_call_at(client):

    sim = Simulation()._attach(client)

    await clear_scene(client)

    results = {}
    def do_smth():
        results['call_time'] = sim.time
        results['call_ticks'] = sim.ticks
        sim.pause()

    sim.call_at(0.1)(do_smth)

    sim.run()

    # await client.run(duration=0.5)
    await asyncio.sleep(0.5)

    assert results['call_time'] == pytest.approx(0.12)
    assert results['call_ticks'] == 3

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_simulation_call_at_with_args(client):

    sim = Simulation()._attach(client)

    await clear_scene(client)

    def do_smth(res):
        res['call_time'] = sim.time
        res['call_ticks'] = sim.ticks
        sim.pause()

    sim.run()

    results = {}

    sim.call_at(0.2)(do_smth, results)

    # await client.run(duration=0.5)
    await asyncio.sleep(0.5)

    assert results['call_time'] == pytest.approx(0.2)
    assert results['call_ticks'] == 5

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_simulation_call_at_step(client):

    sim = Simulation()._attach(client)

    await clear_scene(client)

    results = {}
    def do_smth():
        results['call_time'] = sim.time
        results['call_ticks'] = sim.ticks
        sim.pause()

    sim.call_at_step(5)(do_smth)

    sim.run()

    # await client.run(duration=0.5)
    await asyncio.sleep(0.5)

    assert results['call_time'] == pytest.approx(0.2)
    assert results['call_ticks'] == 5

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_simulation_call_at_step_with_args(client):

    sim = Simulation()._attach(client)

    await clear_scene(client)

    def do_smth(res):
        res['call_time'] = sim.time
        res['call_ticks'] = sim.ticks
        sim.pause()

    sim.run()

    results = {}
    sim.call_at_step(3)(do_smth, results)

    # await client.run(duration=0.5)
    await asyncio.sleep(0.5)

    assert results['call_time'] == pytest.approx(0.12)
    assert results['call_ticks'] == 3

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_simulation_call_each_step(client):

    sim = Simulation()._attach(client)

    await clear_scene(client)

    results = {"steps": 0}
    def do_smth():
        results['steps'] = results['steps'] + 1

    sim.call_each_step()(do_smth)

    sim.step()
    sim.step()
    sim.step()

    # await client.run(duration=0.2)
    await asyncio.sleep(0.2)

    assert results['steps'] == 3

    sim._detach()


@skip_when_no_server_running
@pytest.mark.asyncio
async def test_simulation_call_each_5_steps(client):

    sim = Simulation()._attach(client)

    await clear_scene(client)

    def do_smth(results):
        results['steps'].append(sim.ticks)
        if len(results['steps']) > 5:
            sim.pause()

    results = {"steps": []}

    sim.run()
    sim.maxaccel()
    sim.call_each_step(5)(do_smth, results)

    # await client.run(duration=1.0)
    await asyncio.sleep(1.0)

    assert results['steps'] == [5, 10, 15, 20, 25, 30]

    sim._detach()
