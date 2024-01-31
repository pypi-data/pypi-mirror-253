'''
Copyright (c) 2024 SimTech LLC.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from typing import Optional


from enum import IntEnum

from datetime import datetime, date, time

from . simnettypes import (
    EnvironmentDepth,
    EnvironmentDepthOrder,
    EnvironmentTime,
    EnvironmentTimeOrder,
    EnvironmentTemperatureOrder,
    EnvironmentCurrentOrder,
    EnvironmentWindOrder,
    EnvironmentWaveOrder,
    EnvironmentPrecipitationsOrder,
    EnvironmentWeatherPreset,
)

from . events import Events

from . proxy import SimDataClient


class Temperature(SimDataClient):

    __slots__ = "_data",

    def __init__(self):
        self._data = { 'air': 0, 'water': 0 }

    def _subscribe(self):
        self._client.subscribe(Events.ENVIRONMENT_TEMPERATURE, self._receive)

    def _unsubscribe(self):
        self._client.unsubscribe(Events.ENVIRONMENT_TEMPERATURE, self._receive)

    @property
    def air(self) -> float:
        ''' Returns air temperature (degree Celsius) '''
        return self._data['air']

    @air.setter
    def air(self, value: float) -> None:
        ''' Set air temperature (degree Celsius) '''
        self._data['air'] = value
        self._send(EnvironmentTemperatureOrder.from_dict(self._data))

    @property
    def water(self) -> float:
        ''' Returns water temperature (degree Celsius) '''
        return self._data['water']

    @water.setter
    def water(self, value: float) -> None:
        ''' Set water temperature (degree Celsius) '''
        self._data['water'] = value
        self._send(EnvironmentTemperatureOrder.from_dict(self._data))



class Wind(SimDataClient):

    __slots__ = "_data",

    def __init__(self):
        self._data = { 'direction_from': 0, 'speed': 0 }

    def _subscribe(self):
        self._client.subscribe(Events.ENVIRONMENT_WIND, self._receive)

    def _unsubscribe(self):
        self._client.unsubscribe(Events.ENVIRONMENT_WIND, self._receive)

    @property
    def direction_from(self) -> float:
        ''' Returns wind direction from (radians) '''
        return self._data['direction_from']

    @direction_from.setter
    def direction_from(self, value) -> None:
        ''' Set wind direction from (radians) '''
        self._data['direction_from'] = value
        self._send(EnvironmentWindOrder.from_dict(self._data))

    @property
    def speed(self) -> float:
        ''' Returns wind speed (m/s) '''
        return self._data['speed']

    @speed.setter
    def speed(self, value) -> None:
        ''' Set wind speed (m/s) '''
        self._data['speed'] = value
        self._send(EnvironmentWindOrder.from_dict(self._data))

    def set(self, direction_from: float, speed: float):
        ''' Set wind direction from (radians) and speed (m/s) at once '''
        self._data = { 'direction_from': direction_from, 'speed': speed }
        self._send(EnvironmentWindOrder.from_dict(self._data))


class Current(SimDataClient):

    __slots__ = "_data",

    def __init__(self):
        self._data = { 'direction_to': 0, 'speed': 0 }

    def _subscribe(self):
        self._client.subscribe(Events.ENVIRONMENT_CURRENT, self._receive)

    def _unsubscribe(self):
        self._client.unsubscribe(Events.ENVIRONMENT_CURRENT, self._receive)

    @property
    def direction_to(self) -> float:
        ''' Returns current direction to (radians) '''
        return self._data['direction_to']

    @direction_to.setter
    def direction_to(self, value: float) -> None:
        ''' Set current direction to (radians) '''
        self._data['direction_to'] = value
        self._send(EnvironmentCurrentOrder.from_dict(self._data))

    @property
    def speed(self) -> float:
        ''' Returns current speed (m/s) '''
        return self._data['speed']

    @speed.setter
    def speed(self, value: float) -> None:
        ''' Set current speed (m/s) '''
        self._data['speed'] = value
        self._send(EnvironmentCurrentOrder.from_dict(self._data))

    def set(self, direction_to: float, speed: float):
        ''' Set current direction to (radians) and speed (m/s) at once '''
        self._data = { 'direction_to': direction_to, 'speed': speed }
        self._send(EnvironmentCurrentOrder.from_dict(self._data))


class Wave(SimDataClient):

    __slots__ = "_data",

    def __init__(self):
        self._data = {
            'direction_to': 0.0,
            'wind_speed': 0.0,
            'typical_height': 0.0,
            'typical_length': 0.0,
            'direction_spread': 0.0,
            'number_of_frequencies': 0,
            'number_of_directions': 0
        }

    def _subscribe(self):
        self._client.subscribe(Events.ENVIRONMENT_WAVE, self._receive)

    def _unsubscribe(self):
        self._client.unsubscribe(Events.ENVIRONMENT_WAVE, self._receive)

    @property
    def direction_to(self) -> float:
        ''' Returns wave direction to (radians) '''
        return self._data['direction_to']

    @direction_to.setter
    def direction_to(self, value: float) -> None:
        ''' Set wave direction to (radians) '''
        self._data['direction_to'] = value
        self._send(EnvironmentWaveOrder.from_dict(self._data))

    @property
    def wind_speed(self) -> float:
        ''' Returns wind speed generated the wave (m/s) '''
        return self._data['wind_speed']

    @wind_speed.setter
    def wind_speed(self, value) -> None:
        ''' Set wind speed (m/s) to regenerate wave '''
        self._data['wind_speed'] = value
        self._send(EnvironmentWaveOrder.from_dict(self._data))

    @property
    def typical_height(self) -> float:
        ''' Returns typical wave height (m) '''
        return self._data['typical_height']

    @typical_height.setter
    def typical_height(self, value) -> None:
        ''' Set typical wave height (m) to regenerate wave '''
        self._data['typical_height'] = value
        self._send(EnvironmentWaveOrder.from_dict(self._data))

    @property
    def typical_length(self) -> float:
        ''' Returns typical wave length (m) '''
        return self._data['typical_length']

    @typical_length.setter
    def typical_length(self, value) -> None:
        ''' Set typical wave length (m) to regenerate wave '''
        self._data['typical_length'] = value
        self._send(EnvironmentWaveOrder.from_dict(self._data))

    @property
    def direction_spread(self) -> float:
        ''' Returns wave direction spread (degrees) '''
        return self._data['direction_spread']

    @direction_spread.setter
    def direction_spread(self, value) -> None:
        ''' Set wave direction spread (degrees) to regenerate wave '''
        self._data['direction_spread'] = value
        self._send(EnvironmentWaveOrder.from_dict(self._data))

    @property
    def number_of_frequencies(self) -> int:
        ''' Returns number of frequencies used to generate wave '''
        return self._data['number_of_frequencies']

    @number_of_frequencies.setter
    def number_of_frequencies(self, value) -> None:
        ''' Set number of frequencies to regenerate wave '''
        self._data['number_of_frequencies'] = value
        self._send(EnvironmentWaveOrder.from_dict(self._data))

    @property
    def number_of_directions(self) -> int:
        ''' Returns number of directional components used to generate wave '''
        return self._data['number_of_directions']

    @number_of_directions.setter
    def number_of_directions(self, value) -> None:
        ''' Set number of directional components to regenerate wave '''
        self._data['number_of_directions'] = value
        self._send(EnvironmentWaveOrder.from_dict(self._data))

    def set(self,
            direction_to: Optional[float] = None,
            wind_speed: Optional[float] = None,
            typical_height: Optional[float] = None,
            typical_length: Optional[float] = None,
            direction_spread: Optional[float] = None,
            number_of_frequencies: Optional[int] = None,
            number_of_directions: Optional[int] = None):
        ''' Set wave parameters at once to regenerate the wave '''
        self._data = {
            'direction_to': direction_to if direction_to is not None else self._data['direction_to'],
            'wind_speed': wind_speed if wind_speed is not None else self._data['wind_speed'],
            'typical_height': typical_height if typical_height is not None else self._data['typical_height'],
            'typical_length': typical_length if typical_length is not None else self._data['typical_length'],
            'direction_spread': direction_spread if direction_spread is not None else self._data['direction_spread'],
            'number_of_frequencies': number_of_frequencies if number_of_frequencies is not None else self._data['number_of_frequencies'],
            'number_of_directions': number_of_directions if number_of_directions is not None else self._data['number_of_directions']
        }
        self._send(EnvironmentWaveOrder.from_dict(self._data))


class Precipitations(SimDataClient):

    __slots__ = "_data",

    def __init__(self):
        self._data = { 'fog': 0.0, 'clouds': 0.0, 'rain': 0.0, 'snow': 0.0 }

    def _subscribe(self):
        self._client.subscribe(Events.ENVIRONMENT_PRECIPITATIONS, self._receive)

    def _unsubscribe(self):
        self._client.unsubscribe(Events.ENVIRONMENT_PRECIPITATIONS, self._receive)

    @property
    def fog(self) -> float:
        return self._data['fog']

    @fog.setter
    def fog(self, value) -> None:
        self._data['fog'] = value
        self._send(EnvironmentPrecipitationsOrder.from_dict(self._data))

    @property
    def clouds(self) -> float:
        return self._data['clouds']

    @clouds.setter
    def clouds(self, value) -> None:
        self._data['clouds'] = value
        self._send(EnvironmentPrecipitationsOrder.from_dict(self._data))

    @property
    def rain(self) -> float:
        return self._data['rain']

    @rain.setter
    def rain(self, value) -> None:
        self._data['rain'] = value
        self._send(EnvironmentPrecipitationsOrder.from_dict(self._data))

    @property
    def snow(self) -> float:
        return self._data['snow']

    @snow.setter
    def snow(self, value) -> None:
        self._data['snow'] = value
        self._send(EnvironmentPrecipitationsOrder.from_dict(self._data))



class WeatherPresets(IntEnum):
  ClearSkies = 0
  PartlyCloudy = 1
  Cloudy = 2
  Overcast = 3
  Foggy = 4
  LightRain = 5
  Rain = 6
  Thunderstorm = 7
  LightSnow = 8
  Snow = 9
  Blizzard = 10


class Environment(SimDataClient):

    __slots__ = "_depth", "_time", "_wind", "_wave", "_current", "_weather_preset", "_precipitations", "_temperature"


    def __init__(self):
        self._depth = 0
        self._time = 0
        self._wind = Wind()
        self._wave = Wave()
        self._current = Current()
        self._weather_preset = WeatherPresets.ClearSkies
        self._precipitations = Precipitations()
        self._temperature = Temperature()

    def _subscribe(self):
        self._client.subscribe(Events.ENVIRONMENT_DEPTH, self.on_depth)
        self._client.subscribe(Events.ENVIRONMENT_TIME, self.on_time)
        self._client.subscribe(Events.ENVIRONMENT_WEATHER_PRESET, self.on_weather_preset)
        self._temperature._attach(self._client)
        self._wind._attach(self._client)
        self._wave._attach(self._client)
        self._current._attach(self._client)
        self._precipitations._attach(self._client)

    def _unsubscribe(self):
        self._client.unsubscribe(Events.ENVIRONMENT_DEPTH, self.on_depth)
        self._client.unsubscribe(Events.ENVIRONMENT_TIME, self.on_time)
        self._client.unsubscribe(Events.ENVIRONMENT_WEATHER_PRESET, self.on_weather_preset)
        self._temperature._detach()
        self._wind._detach()
        self._wave._detach()
        self._current._detach()
        self._precipitations._detach()
        return self

    @property
    def datetime(self) -> datetime:
        return datetime.fromtimestamp(self._time)

    @property
    def date(self) -> date:
        return self.datetime.date()

    @property
    def daytime(self) -> time:
        return self.datetime.time()

    @property
    def time(self) -> float:
        return self._time

    @time.setter
    def time(self, value) -> None:
        self._time = value
        self._send(EnvironmentTimeOrder(value))

    @property
    def depth(self) -> float:
        return self._depth

    @depth.setter
    def depth(self, value) -> None:
        self._depth = value
        self._send(EnvironmentDepthOrder(value))

    @property
    def weather_preset(self) -> WeatherPresets:
        return self._weather_preset

    @weather_preset.setter
    def weather_preset(self, value) -> None:
        self._weather_preset = value
        self._send(EnvironmentWeatherPreset(value))

    @property
    def temperature(self) -> Temperature:
        return self._temperature

    @property
    def wind(self) -> Wind:
        return self._wind

    @property
    def wave(self) -> Wave:
        return self._wave

    @property
    def current(self) -> Current:
        return self._current

    @property
    def precipitations(self) -> Precipitations:
        return self._precipitations


    #
    # Simulation server events handlers
    #

    def on_time(self, state: EnvironmentTime):
        self._time = state.time

    def on_depth(self, state: EnvironmentDepth):
        self._depth = state.depth

    def on_weather_preset(self, state: EnvironmentWeatherPreset):
        self._weather_preset = state.preset

