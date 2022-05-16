# -*- coding: utf-8 -*-
"""curiousLiDAR Main"""
__copyright__ = ("Copyright (c) 2022 David Dias Horta, Paul Meier")

# on windows:
#   mypy .
#   pylint main.py lidar.py rovex.py asyncThread.py findShapes.py

from argparse import ArgumentParser
import argparse
import os
import sys

import time

from aiohttp import web
from aiohttp_index import IndexMiddleware
from findShapes import contest_pop_loon # type: ignore
from lidar import LiDAR

from rovex import Rover

argumentParser = ArgumentParser(description="Python Basic Webserver")

argumentParser.add_argument("-b", "--bypass-timeout",
    action=argparse.BooleanOptionalAction, # type: ignore
    help="bypass startup timeout")

argumentParser.add_argument("-p", "--port",
    required=False,
    default=8080,
    help="port")

argumentParser.add_argument("-l", "--lidar",
    required=False,
    default="/dev/ttyUSB0",
    help="lidar com (e.g. COM6, /dev/xy, ...)")

argumentParser.add_argument("-r", "--rover",
    required=False,
    default="/dev/ttyACM0",
    help="rover com (e.g. COM6, /dev/xy, ...)")

arguments = argumentParser.parse_args() # get arguments

if arguments.bypass_timeout:
    print("bypassing startup timeout")
else:
    print("starting in 10s (press [CTRL]+[C] to cancel)")
    time.sleep(10)
    print("starting...")

rover = Rover(arguments.rover)
lidar = LiDAR(arguments.lidar)

async def getDataHandler(_: web.Request) -> web.Response:
    """gets the current LiDAR data"""
    return web.json_response(status = 200, data = lidar.data.toJson())

async def exitHandler(_: web.Request) -> web.Response:
    """force quits the application"""
    print("exiting")
    os._exit(10) # pylint: disable=protected-access

async def restartHandler(_: web.Request) -> web.Response:
    """force restarts the application"""
    print("restarting")
    os.execl(sys.executable, sys.executable, *sys.argv)

async def setSpeedsHandler(request: web.Request) -> web.Response:
    """sets the rover's speeds"""
    data = await request.json()
    speedL = data["speedL"]
    speedR = data["speedR"]
    print(f"speedL={speedL}, speedR={speedR}")
    rover.setSpeeds(speedL, speedR)
    return web.Response()

async def getRecommendedSpeeds(request: web.Request) -> web.Response:
    """gets the recommended speeds (L, R)"""
    speedL, speedR = contest_pop_loon(lidar.data.toJson())
    print(f"speedL={speedL}, speedR={speedR}")
    return web.json_response(status = 200, data = {
        "speedL": speedL,
        "speedR": speedR
    })

app = web.Application(middlewares=[IndexMiddleware()])

app.router.add_get('/data', getDataHandler)
app.router.add_get('/auto', getRecommendedSpeeds)
app.router.add_get('/system/exit', exitHandler)
app.router.add_get('/system/reboot', restartHandler)
app.router.add_post('/rover/speed', setSpeedsHandler)

app.router.add_static('/', './ui/dist')

app.on_startup.append(lidar.startupTask)
web.run_app(app, port = arguments.port)
