# -*- coding: utf-8 -*-
"""curiousLiDAR self drive"""
__copyright__ = ("Copyright (c) 2022 David Dias Horta, Paul Meier")

import asyncio
import time

from aiohttp import web

from asyncThread import asyncRunInThread
from findShapes import findContestBalloon
from lidar import LiDAR
from rovex import Rover, Speed


class SelfDrive:
    """selfDrive (automated driving)"""
    def __init__(self, rover: Rover, lidar: LiDAR, default: bool = False):
        self._rover = rover
        self._lidar = lidar
        self._enabled = default
        self._alternateAngle = False

    @property
    def enabled(self) -> bool:
        """whether it's enabled or not"""
        return self._enabled

    async def onEnableHandler(self, _: web.Request) -> web.Response:
        """enable selfDrive"""
        self._alternateAngle = False
        self._enabled = True
        return web.Response()

    async def onDisableHandler(self, _: web.Request) -> web.Response:
        """enable selfDrive"""
        self._enabled = False
        self._rover.setSpeeds(Speed.N.value, Speed.N.value)
        return web.Response()

    def _backAndTurnRight(self) -> None:
        self._alternateAngle = not self._alternateAngle
        self._rover.setSpeeds(Speed.R5.value, Speed.R5.value)
        time.sleep(1)
        self._rover.setSpeeds(Speed.D4.value,Speed.R4.value)
        time.sleep(0.6)
        self._rover.setSpeeds(Speed.N.value, Speed.N.value)

    async def startupTask(self, _: web.Application) -> None:
        """runs the contest balloon continuously"""
        def _implement() -> None:
            while True:
                time.sleep(0.2) # 200 ms
                if not self._enabled:
                    continue
                value = findContestBalloon(self._lidar.data.toJson(), self._alternateAngle)
                print("#######################")
                print(value)
                if isinstance(value, tuple):
                    if Speed.I in value:
                        self._backAndTurnRight()
                        continue

                    speedL, speedR = value
                    print(f"speedL={speedL}, speedR={speedR}")
                    self._rover.setSpeeds(speedL.value, speedR.value)
        asyncio.create_task(asyncRunInThread(_implement))
