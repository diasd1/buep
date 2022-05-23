# -*- coding: utf-8 -*-
"""curiousLiDAR Main"""
__copyright__ = ("Copyright (c) 2022 David Dias Horta, Paul Meier")

# on windows:
#   mypy .
#   pylint main.py lidar.py rovex.py asyncThread.py findShapes.py

from argparse import ArgumentParser
import argparse
import asyncio
import os
import sys

import time

from aiohttp import web
from aiohttp_index import IndexMiddleware # type: ignore
from asyncThread import asyncRunInThread
from findShapes import findContestBalloon
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

autoRun = False

async def enableAuto(_: web.Request) -> web.Response:
    """enable 'auto'"""
    global autoRun
    autoRun = True
    return web.Response()

async def disableAuto(_: web.Request) -> web.Response:
    """disables 'auto'"""
    global autoRun
    autoRun = True
    return web.Response()

async def autoLoop(_: web.Application) -> None:
    """runs the contest balloon continuously"""
    def _implement() -> None:
        while True:
            time.sleep(0.2) # 100 ms
            if not autoRun:
                continue
            speedL, speedR = findContestBalloon(lidar.data.toJson())
            print(f"speedL={speedL}, speedR={speedR}")
            rover.setSpeeds(speedL.value, speedR.value)
    asyncio.create_task(asyncRunInThread(_implement))

app = web.Application(middlewares=[IndexMiddleware()])

app.router.add_get('/data', getDataHandler)
app.router.add_get('/auto/enable', enableAuto)
app.router.add_get('/auto/disable', disableAuto)
app.router.add_get('/system/exit', exitHandler)
app.router.add_get('/system/reboot', restartHandler)
app.router.add_post('/rover/speed', setSpeedsHandler)

app.router.add_static('/', './ui/dist')

app.on_startup.append(lidar.startupTask)
app.on_startup.append(autoLoop)
web.run_app(app, port = arguments.port)
