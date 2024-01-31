import pytest
import pytest_asyncio
import asyncio

from datetime import datetime, timedelta

from conftest import skip_when_no_server_running, real_server_config

from ashapi.simrequests import(
    SceneClear as RequestSceneClear,
    SceneNew as RequestSceneNew,
    SceneOpen as RequestSceneOpen,
)

from ashapi.client import SimcomplexClient
from ashapi.simulation import Simulation
from ashapi.environment import Environment, WeatherPresets

from ashapi import math2


pytestmark = pytest.mark.asyncio(scope="module")


@pytest_asyncio.fixture(scope='module') 
async def client():
    '''Arrange client connected to server'''
    client = SimcomplexClient(real_server_config)
    await client.connect()
    asyncio.create_task(client.run())
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

async def do_step(client, delay=0.1):
    sim = Simulation()._attach(client)
    sim.step()
    await asyncio.sleep(delay)


@skip_when_no_server_running
async def test_environment_time_load_empty(client):

    env = Environment()
    env._attach(client)

    await load_scene(client, 'api/empty.stexc')

    date = env.datetime

    assert date.year == 2023
    assert date.month == 12
    assert date.day == 1
    assert date.hour == 12
    assert date.minute == 0
    assert date.second == 0

    env._detach()


@skip_when_no_server_running
async def test_environment_clear_scene(client):

    env = Environment()
    env._attach(client)

    await clear_scene(client)

    # Time

    now = datetime.now()

    assert env.datetime < now

    assert now - env.datetime < timedelta(seconds=1.5)

    # Temperature

    assert env.temperature.air == 20.0
    assert env.temperature.water == 15.0

    # Depth

    assert env.depth == 100.0

    # Wind

    assert env.wind.direction_from == 0.0
    assert env.wind.speed == 0.0

    # Wave

    wave = env.wave

    assert wave.direction_to == 0.0
    assert wave.wind_speed == 0.0
    assert wave.typical_height == 0.0
    assert wave.direction_spread == 0.0
    assert wave.number_of_frequencies == 0
    assert wave.number_of_directions == 0

    # Current

    assert env.current.direction_to == 0.0
    assert env.current.speed == 0.0

    # Precipitations

    prec = env.precipitations

    assert prec.fog == 0.0
    assert prec.clouds == 0.0
    assert prec.rain == 0.0
    assert prec.snow == 0.0

    # Weather Preset

    assert env.weather_preset == 0
    assert env.weather_preset == WeatherPresets.ClearSkies

    env._detach()


@skip_when_no_server_running
async def test_environment_load_conditions(client):

    env = Environment()
    env._attach(client)

    await load_scene(client, 'api/environment/environment_conditions.stexc')

    # Time

    date = env.datetime

    assert date.year == 2023
    assert date.month == 12
    assert date.day == 15
    assert date.hour == 10
    assert date.minute == 20
    assert date.second == 35

    # Temperature

    assert env.temperature.air == 22.0
    assert env.temperature.water == 18.0

    # Depth

    assert env.depth == 50.0

    # Wind

    assert math2.rad2deg(env.wind.direction_from) == pytest.approx(30.0)
    assert math2.msec2knots(env.wind.speed) == pytest.approx(10.0)

    # Wave

    wave = env.wave

    assert math2.rad2deg(wave.direction_to) == pytest.approx(215.0)
    assert math2.msec2knots(wave.wind_speed) ==  pytest.approx(18.35378)
    assert wave.typical_height == pytest.approx(2.0)
    assert math2.rad2deg(wave.direction_spread) == pytest.approx(30.0)
    assert wave.number_of_frequencies == 15
    assert wave.number_of_directions == 11

    # Current

    assert math2.rad2deg(env.current.direction_to) == 200.0
    assert math2.msec2knots(env.current.speed) == 5.0

    # Precipitations

    prec = env.precipitations

    assert prec.fog == 0.3
    assert prec.clouds == 0.8
    assert prec.rain == 0.7
    assert prec.snow == 0.1

    # Weather Preset

    assert env.weather_preset == 7
    assert env.weather_preset == WeatherPresets.Thunderstorm

    env._detach()


@skip_when_no_server_running
async def test_environment_set_time_depth_weather(client):

    env = Environment()
    env._attach(client)

    await clear_scene(client)

    date = datetime(2025, 6, 23, 4, 32, 55)
    t = date.timestamp()

    test_env = Environment()._attach(client) # new needed, to check that changed applied

    env.time = t
    env.depth = 1.0
    env.weather_preset = WeatherPresets.Blizzard
    env.temperature.air = 32.5
    env.temperature.water = 23.3

    await asyncio.sleep(0.1)

    date = test_env.datetime

    assert date.year == 2025
    assert date.month == 6
    assert date.day == 23
    assert date.hour == 4
    assert date.minute == 32
    assert date.second == 55

    assert test_env.depth == env.depth

    assert test_env.weather_preset == WeatherPresets.Blizzard

    assert test_env.temperature.air == env.temperature.air
    assert test_env.temperature.water == env.temperature.water

    env._detach()
    test_env._detach()


@skip_when_no_server_running
async def test_environment_set_wind_current(client):

    env = Environment()
    env._attach(client)

    await clear_scene(client)

    test_env = Environment()._attach(client) # new needed, to check that changed applied

    env.wind.direction_from = 1.57 / 2
    env.wind.speed = 2

    env.current.direction_to = 1.57 / 4
    env.current.speed = 1.5

    # await do_step(client)
    await asyncio.sleep(0.1)

    assert test_env.wind.direction_from == env.wind.direction_from 
    assert test_env.wind.speed == env.wind.speed

    assert test_env.current.direction_to == env.current.direction_to
    assert test_env.current.speed == env.current.speed

    env._detach()
    test_env._detach()


@skip_when_no_server_running
async def test_environment_set_waves(client):

    env = Environment()
    env._attach(client)

    await clear_scene(client)

    test_env = Environment()._attach(client) # new needed, to check that changed applied

    env.wave.number_of_directions = 7
    env.wave.number_of_frequencies = 8
    env.wave.direction_spread = 0.52
    env.wave.direction_to = 0.49
    env.wave.typical_height = 1.5

    await do_step(client)
    env.wave.direction_to = 0.41
    await do_step(client)

    assert math2.msec2knots(env.wave.wind_speed) == pytest.approx(15.89483)

    assert test_env.wave.number_of_directions == env.wave.number_of_directions
    assert test_env.wave.number_of_frequencies == env.wave.number_of_frequencies
    assert test_env.wave.direction_spread == env.wave.direction_spread
    assert test_env.wave.direction_to == env.wave.direction_to
    assert test_env.wave.typical_height == env.wave.typical_height
    assert test_env.wave.typical_length == pytest.approx(58.492998)

    env.wave.wind_speed = 5

    await do_step(client)

    assert env.wave.typical_height == pytest.approx(0.560844)
    assert env.wave.typical_length == pytest.approx(21.87029444)

    env.wave.typical_length = 80.0

    await do_step(client)

    assert env.wave.wind_speed == pytest.approx(9.562857469)
    assert env.wave.typical_height == pytest.approx(2.051527598)

    env._detach()
    test_env._detach()
