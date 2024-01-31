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

from dataclasses import dataclass

import os.path

#
# Configuration of ashapi client
#

@dataclass
class Config:

    host: str
    port: int
    autoreconnect: bool # whether to make attempts to reconnect to server if connection has failed
    simcomplex: str     # path to local simcomplex installation


    @classmethod
    def localhost(cls,
                  port = 3000,
                  autoreconnect = False,
                  simcomplex = "C:\Program Files\SimTech\simcomplex"):

        config = cls('localhost', port, autoreconnect, simcomplex)
        return config


    @classmethod
    def lab(cls,
            port=3000,
            autoreconnect = False):
        config = cls('lab.simcomplex.com', port, autoreconnect, "")
        return config


    @property
    def authority(self):
        return f"{self.host}:{self.port}"

    @property
    def protocol(self):
        return 'http'

    @property
    def http_uri(self):
        return f"http://{self.authority}"

    @property
    def ws_uri(self):
        return f"ws://{self.authority}{self.ws_resource}"

    @property
    def ws_resource(self):
        return f"/data/wss"
    
    @property
    def local_server_path(self):
        if os.path.exists(self.simcomplex):
            return os.path.join(self.simcomplex, "simserver")
        return ""
