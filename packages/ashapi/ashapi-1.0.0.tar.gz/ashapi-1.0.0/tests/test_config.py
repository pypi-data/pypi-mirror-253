import pytest

from ashapi.config import Config


config_test_data = [
    (
        Config.localhost(), 
        {
            'host': 'localhost',
            'port': 3000,
            'authority': "localhost:3000",
            'ws_uri': "ws://localhost:3000/data/wss",
            'local_server_path': "C:\Program Files\SimTech\simcomplex\simserver"
        }
    ),
    (
        Config.localhost(port=3001),
        {
            'host': 'localhost',
            'port': 3001,
            'authority': "localhost:3001",
            'ws_uri': "ws://localhost:3001/data/wss",
            'local_server_path': "C:\Program Files\SimTech\simcomplex\simserver"
        }
    ),
    (
        Config.lab(),
        {
            'host': 'lab.simcomplex.com',
            'port': 3000,
            'authority': "lab.simcomplex.com:3000",
            'ws_uri': "ws://lab.simcomplex.com:3000/data/wss",
            'local_server_path': ""
        }
    ),
    (
        Config.lab(port=3001),
        {
            'host': 'lab.simcomplex.com',
            'port': 3001,
            'authority': "lab.simcomplex.com:3001",
            'ws_uri': "ws://lab.simcomplex.com:3001/data/wss",
            'local_server_path': ""
        }
    ),
]


@pytest.mark.parametrize("conf, expected", config_test_data)
def test_config_construction(conf, expected):

    assert conf.host == expected['host']
    assert conf.port == expected['port']
    assert conf.authority == expected['authority']
    assert conf.ws_uri == expected['ws_uri']
    assert conf.local_server_path == expected['local_server_path']

