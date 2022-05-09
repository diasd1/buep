from argparse import ArgumentParser
import argparse
import os
import sys

import time
import serial
import asyncio

from aiohttp import web
from aiohttp_index import IndexMiddleware

from asyncThread import asyncRunInThread
from rovex import Rover
from uart import LiDARCurrentData, LiDARMessage

argumentParser = ArgumentParser(description="Python Basic Webserver")
argumentParser.add_argument("-b", "--bypass-timeout", action=argparse.BooleanOptionalAction, help="bypass startup timeout")
argumentParser.add_argument("-p", "--port", required=False,
    default=8080, help="port")
argumentParser.add_argument("-l", "--lidar", required=False,
    default="/dev/ttyUSB0", help="lidar com (e.g. COM6, /dev/xy, ...)")
argumentParser.add_argument("-r", "--rover", required=False,
    default="/dev/ttyACM0", help="rover com (e.g. COM6, /dev/xy, ...)")
arguments = argumentParser.parse_args() # get arguments

if arguments.bypass_timeout:
    print("bypassing startup timeout")
else:
    print("starting in 10s (press [CTRL]+[C] to cancel)")
    time.sleep(10)
    print("starting...")

data = LiDARCurrentData()
msg = LiDARMessage(data)

async def getHandler(_: web.Request) -> web.Response:
    return web.json_response(status = 200, data = data._dist)

async def exitHandler(_: web.Request) -> None:
    print("exiting")
    os._exit(10)

async def restartHandler(_: web.Request) -> web.Response:
    print("restarting")
    os.execl(sys.executable, sys.executable, *sys.argv)

rover = Rover(arguments.rover)

async def setSpeeds(request: web.Request) -> web.Response:
    data = await request.json()
    speedL = data["speedL"]
    speedR = data["speedR"]
    print(f"speedL={speedL}, speedR={speedR}")
    rover.setSpeeds(speedL, speedR)
    return web.Response()

app = web.Application(middlewares=[IndexMiddleware()])

app.router.add_get('/data', getHandler)
app.router.add_get('/system/exit', exitHandler)
app.router.add_get('/system/reboot', restartHandler)
app.router.add_post('/rover/speed', setSpeeds)

app.router.add_static('/', './ui/dist')

async def _serialLoop(_: web.Application):
    def _implement():
        while True:
            try:
                ser = serial.Serial(arguments.lidar, 115200)

                while True:
                    cc = ser.read()
                    msg.update(int.from_bytes(cc, "big"))
            except Exception as e:
                print(e)
                time.sleep(2)
    asyncio.create_task(asyncRunInThread(_implement, []))

app.on_startup.append(_serialLoop)
asyncio.run ( web._run_app(app, port=arguments.port) )
