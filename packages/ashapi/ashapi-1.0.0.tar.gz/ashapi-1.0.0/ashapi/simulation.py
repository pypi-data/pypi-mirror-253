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

from typing import Optional, Callable

from . simrequests import SimulationState as SimulationStateRequest, RecordingSeek
from . simnettypes import SimulationState

from . proxy import SimDataClient

from . events import Events
from . timer import keepfunc


class Simulation(SimDataClient):

    __slots__ = "_state"

    def __init__(self):
        self._state = SimulationState()

    def _subscribe(self):
        self._client.subscribe(Events.SIMULATION_STATE, self.on_state_changed)

    def _unsubscribe(self):
        self._client.unsubscribe(Events.SIMULATION_STATE, self.on_state_changed)

    @property
    def is_running(self) -> bool:
        return self._state.running

    @property
    def is_paused(self) -> bool:
        return not self.is_running

    @property
    def is_recording(self) -> bool:
        ''' Whether simulation is currently being recorded (so that recording could be saved later) '''
        return self._state.recording

    @property
    def is_playback(self) -> bool:
        ''' Whether simulation is currently in playback state (no simulation, recording is loaded) '''
        return self._state.playback

    @property
    def duration(self) -> float:
        ''' Returns total duration in seconds (for playback state only) '''
        return self._state.duration

    @property
    def time(self) -> float:
        ''' Current simulation time (seconds), counted from start of current simulation '''
        return self._state.time

    @property
    def time_zero(self) -> float:
        '''
        Simulation time start point (seconds) - time from previous simulation.
        Can be non-zero when after excercise with previous simulation loaded.
        '''
        return self._state.start

    @property
    def time_total(self) -> float:
        ''' Total simulation time (seconds), including both current simulation time and time_zero '''
        return self.time_zero + self.time

    @property
    def ticks(self) -> int:
        ''' Number of simulation ticks (steps) made in current simulation '''
        return self._state.ticks

    @property
    def time_ratio(self) -> int:
        ''' Real time ratio of simulation speed versus real time speed '''
        return self._state.realaccel

    @property
    def is_maxaccel(self) -> bool:
        return self._state.maxaccel

    @property
    def accel(self) -> float:
        ''' Time ratio (simulation speed versus real time speed) set (requested) '''
        return self._state.accel

    #
    # Requests to simulation server
    #

    def run(self,
            on_response: Callable[[str], None] = lambda response_text: None):
        self._request(SimulationStateRequest.run(), on_response)

    def setaccel(self,
                 accel: float = 1.0,
                 on_response: Callable[[str], None] = lambda response_text: None):
        if self._client:
            self._client.send_request(SimulationStateRequest.accel(accel), on_response)

    def maxaccel(self,
                 on_response: Callable[[str], None] = lambda response_text: None):
        self._request(SimulationStateRequest.maxaccel(), on_response)

    def pause(self,
              on_response: Callable[[str], None] = lambda response_text: None):
        self._request(SimulationStateRequest.pause(), on_response)

    def step(self,
             on_response: Callable[[str], None] = lambda response_text: None):
        self._request(SimulationStateRequest.step(), on_response)

    def seek(self,
             time: float,
             on_response: Callable[[str], None] = lambda response_text: None):
        self._request(RecordingSeek(time), on_response)

    #
    # Simulation server events handlers
    #

    def on_state_changed(self, state: SimulationState):
        self._state = state
        # print(f"Simulation got state: {state}")

    #
    # Simulation time events & subscriptions
    #

    def call_at(self, t: float) -> Callable:
        '''
        Schedule call at (after) simulation time t (sec)
        Usage:
            def do_smth([arg1][,...]):
                # do something useful
            simulation.call_at(5.0)(do_smth [,arg1][,...])
        '''
        call_me = keepfunc()
        def on_time_changed(state: SimulationState):
            if state.time >= t:
                if call_me.func is not None:
                    # ensure simulation state updated if this event happened before on_state_changed
                    self.on_state_changed(state)
                    call_me.func(*call_me.args)
                self._client.eventbus.remove_listener(Events.SIMULATION_STATE, on_time_changed)
        self._client.eventbus.add_listener(Events.SIMULATION_STATE, on_time_changed)
        return call_me


    def call_at_step(self, i: int) -> Callable:
        '''
        Schedule call at particular simulation step i.
        Usage:
            def do_smth([arg1][,...]):
                # do something useful
            simulation.call_at_step(5)(do_smth [,arg1][,...])
        '''
        call_me = keepfunc()
        def on_ticks_changed(state: SimulationState):
            if state.ticks == i:
                if call_me.func is not None:
                    # ensure simulation state updated if this event happened before on_state_changed
                    self.on_state_changed(state)
                    call_me.func(*call_me.args)
                self._client.eventbus.remove_listener(Events.SIMULATION_STATE, on_ticks_changed)
        self._client.eventbus.add_listener(Events.SIMULATION_STATE, on_ticks_changed)
        return call_me


    def call_each_step(self, i: int = 1) -> Callable:
        '''
        Schedule call at each sth simulation step i.
        Usage:
            def do_smth([arg1][,...]):
                # do something useful
            simulation.call_each_step()(do_smth [,arg1][,...]) # will call do_smth each step
            simulation.call_each_step(5)(do_smth [,arg1][,...]) # will call do_smth each 5 steps
        '''
        call_me = keepfunc()
        next_tick = i
        def on_ticks_reached(state: SimulationState):
            nonlocal next_tick
            if state.ticks == next_tick:
                if call_me.func is not None:
                    # ensure simulation state updated if this event happened before on_state_changed
                    self.on_state_changed(state)
                    call_me.func(*call_me.args)
                next_tick += i
        self._client.eventbus.add_listener(Events.SIMULATION_STATE, on_ticks_reached)
        return call_me

    #
    # Simulation running additional control
    #

    def run_until(self, t: float):
        ''' Run simulation until t seconds of simulation time and then pause '''
        if not self.is_running:
            self.run()
        self.call_at(t)(self.pause)

    def run_for(self,
                t: float,
                end_action: Optional[Callable] = None):
        '''
        Run simulation for t seconds (counting from current simulation time) and then pause.
        Optionally call end_action() (if provided) prior pausing.
        '''
        if not self.is_running:
            self.run()
            def do_action():
                if end_action is not None and callable(end_action):
                    end_action()
                self.pause()
        self.call_at(self.time + t)(do_action)