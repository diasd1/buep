from argparse import ArgumentParser
import os
import sys

import time
import serial
import asyncio

from aiohttp import web
from aiohttp_index import IndexMiddleware

from asyncThread import asyncRunInThread
from uart import LiDARCurrentData, LiDARMessage

argumentParser = ArgumentParser(description="Python Basic Webserver")
argumentParser.add_argument("-p", "--port", required=False,
default=8080, help="port")
arguments = argumentParser.parse_args() # get arguments

data = LiDARCurrentData()
msg = LiDARMessage(data)

async def getHandler(_: web.Request) -> web.Response:
    return web.json_response(status = 200, data = data._dist)

async def exitHandler(_: web.Request) -> web.Response:
    print("exiting")
    os._exit(10)
    return web.json_response(status = 200, data = data._dist)

async def restartHandler(_: web.Request) -> web.Response:
    print("restarting")
    os.execl(sys.executable, sys.executable, *sys.argv)

app = web.Application(middlewares=[IndexMiddleware()])

app.router.add_get('/data', getHandler)
app.router.add_get('/system/exit', exitHandler)
app.router.add_get('/system/reboot', restartHandler)

app.router.add_static('/', './ui/dist')

async def _serialLoop(_: web.Application):
    def _implement():
        while True:
            try:
                ser = serial.Serial("COM6", 115200)

                while True:
                    cc = ser.read()
                    msg.update(int.from_bytes(cc, "big"))
            except Exception as e:
                time.sleep(2)
                print(e)
    asyncio.create_task(asyncRunInThread(_implement, []))

async def _driveLoop(_: web.Application):
    def _implement():
        ser = serial.Serial("COM5", 115200)
    asyncio.create_task(asyncRunInThread(_implement, []))

app.on_startup.append(_serialLoop)
asyncio.run ( web._run_app(app, port=arguments.port) )
