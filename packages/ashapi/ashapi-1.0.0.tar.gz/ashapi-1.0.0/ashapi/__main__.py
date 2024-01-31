
import os
import logging
import asyncio

from time import time
from datetime import datetime

from ashapi.config import Config
from ashapi.client import connected
from ashapi.simcomplex import SimcomplexTask, local_server

async def main():

    print(f"STARTED as process with PID={os.getpid()} at {datetime.fromtimestamp(time())}")

    logger = logging.getLogger("ashapi.client")
    logger.setLevel(logging.DEBUG)

    config = Config.localhost(autoreconnect = True)

    async with connected(config):
        pass


if __name__ == "__main__":

    with local_server(Config.localhost()):

        asyncio.run(main(), debug=True)



