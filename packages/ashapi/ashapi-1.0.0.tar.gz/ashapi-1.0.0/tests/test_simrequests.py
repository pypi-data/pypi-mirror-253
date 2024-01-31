
from ashapi import simrequests

from ashapi.simrequests import REQUESTS


def test_all_requests():

    assert len(REQUESTS) == 16    # correct each time when new request is defined (and add assertion below)

    assert '/areas'               in      REQUESTS
    assert '/areas/image'         in      REQUESTS
    assert '/area/map'            in      REQUESTS

    assert '/exercises'           in      REQUESTS

    assert '/models'              in      REQUESTS
    assert '/models/image'        in      REQUESTS

    assert '/recordings'          in      REQUESTS
    assert '/recording/open'      in      REQUESTS
    assert '/recording/save'      in      REQUESTS
    assert '/recording/seek'      in      REQUESTS
    assert '/recording/switch'    in      REQUESTS

    assert '/scene/clear'         in      REQUESTS
    assert '/scene/new'           in      REQUESTS
    assert '/scene/open'          in      REQUESTS
    assert '/scene/save'          in      REQUESTS

    assert '/simulation/state'    in      REQUESTS


def test_SimulationState_run():

    run = simrequests.SimulationState.run()

    assert run.method == 'PATCH'
    assert run.resource == '/simulation/state'
    assert run.params == { 'command': 'run' }


def test_SimulationState_accel():

    run = simrequests.SimulationState.accel(10)

    assert run.method == 'PATCH'
    assert run.resource == '/simulation/state'
    assert run.params == { 'command': 'accel', 'accel': 10 }


def test_SimulationState_maxaccel():

    run = simrequests.SimulationState.maxaccel()

    assert run.method == 'PATCH'
    assert run.resource == '/simulation/state'
    assert run.params == { 'command': 'maxaccel' }


def test_SimulationState_pause():

    run = simrequests.SimulationState.pause()

    assert run.method == 'PATCH'
    assert run.resource == '/simulation/state'
    assert run.params == { 'command': 'pause' }


def test_SimulationState_step():

    run = simrequests.SimulationState.step()

    assert run.method == 'PATCH'
    assert run.resource == '/simulation/state'
    assert run.params == { 'command': 'step' }


def test_SceneClear():

    clear = simrequests.SceneClear()

    assert clear.method == 'POST'
    assert clear.resource == '/scene/clear'
    assert clear.params == {}


def test_SceneNew():

    new = simrequests.SceneNew()

    assert new.method == 'POST'
    assert new.resource == '/scene/new'
    assert new.params == {}


def test_SceneNew_path():

    new = simrequests.SceneNew(r'\some\path')

    assert new.method == 'POST'
    assert new.resource == '/scene/new'
    assert new.params == { 'path': r'\some\path' }


def test_SceneOpen():

    open = simrequests.SceneOpen('one-object.stexc')

    assert open.method == 'POST'
    assert open.resource == '/scene/open'
    assert open.params == { 'path': 'one-object.stexc' }


def test_SceneSave():

    save = simrequests.SceneSave('api\\saved.stexc')

    assert save.method == 'POST'
    assert save.resource == '/scene/save'
    assert save.params == { 'path': 'api\\saved.stexc' }


def test_Recordings():

    rec = simrequests.Recordings()

    assert rec.method == 'GET'
    assert rec.resource == '/recordings'
    assert rec.params == {}


def test_RecordingSwitch():

    rec = simrequests.RecordingSwitch()

    assert rec.method == 'POST'
    assert rec.resource == '/recording/switch'
    assert rec.params == {}


def test_RecordingSeek():

    rec = simrequests.RecordingSeek(10)

    assert rec.method == 'POST'
    assert rec.resource == '/recording/seek'
    assert rec.params == { 'time': 10 }


def test_RecordingOpen():

    rec = simrequests.RecordingOpen('one-object.strec')

    assert rec.method == 'POST'
    assert rec.resource == '/recording/open'
    assert rec.params == { 'path': 'one-object.strec' }


def test_RecordingSave():

    rec = simrequests.RecordingSave('api\\recording_saved.strec')

    assert rec.method == 'POST'
    assert rec.resource == '/recording/save'
    assert rec.params == { 'path': 'api\\recording_saved.strec' }


def test_Areas():

    a = simrequests.Areas()

    assert a.method == 'GET'
    assert a.resource == '/areas'
    assert a.params == {}


def test_AreaImage():

    a = simrequests.AreaImage("NV")

    assert a.method == 'GET'
    assert a.resource == '/areas/image'
    assert a.params == { 'code': "NV" }


def test_AreaMap():

    a = simrequests.AreaMap("NV", "RU6MELN0")

    assert a.method == 'GET'
    assert a.resource == '/area/map'
    assert a.params == { 'code': "NV", 'map': "RU6MELN0" }


def test_Exercises():

    e = simrequests.Exercises()

    assert e.method == 'GET'
    assert e.resource == '/exercises'
    assert e.params == {}


def test_Models():

    m = simrequests.Models()

    assert m.method == 'GET'
    assert m.resource == '/models'
    assert m.params == {}


def test_ModelImage():

    a = simrequests.ModelImage("misv01")

    assert a.method == 'GET'
    assert a.resource == '/models/image'
    assert a.params == { 'code': "misv01" }


