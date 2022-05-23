# -*- coding: utf-8 -*-
"""curiousLiDAR self drive"""
__copyright__ = ("Copyright (c) 2022 David Dias Horta, Paul Meier")

import asyncio
import time

from aiohttp import web

from asyncThread import asyncRunInThread
from findShapes import findContestBalloon
from lidar import LiDAR
from rovex import Rover


class SelfDrive:
    """selfDrive (automated driving)"""
    def __init__(self, rover: Rover, lidar: LiDAR, default: bool = False):
        self._rover = rover
        self._lidar = lidar
        self._enabled = default

    @property
    def enabled(self) -> bool:
        """whether it's enabled or not"""
        return self._enabled

    async def onEnableHandler(self, _: web.Request) -> web.Response:
        """enable selfDrive"""
        self._enabled = True
        return web.Response()

    async def onDisableHandler(self, _: web.Request) -> web.Response:
        """enable selfDrive"""
        self._enabled = False
        self._rover.setSpeeds(0, 0)
        return web.Response()

    async def startupTask(self, _: web.Application) -> None:
        """runs the contest balloon continuously"""
        def _implement() -> None:
            while True:
                time.sleep(0.2) # 200 ms
                if not self._enabled:
                    continue
                speedL, speedR = findContestBalloon(self._lidar.data.toJson())
                print(f"speedL={speedL}, speedR={speedR}")
                self._rover.setSpeeds(speedL.value, speedR.value)
        asyncio.create_task(asyncRunInThread(_implement))
