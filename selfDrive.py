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

    def _backAndExit(self) -> None:
        self._alternateAngle = not self._alternateAngle
        # back
        self._rover.setSpeeds(Speed.R5.value, Speed.R5.value)
        time.sleep(0.5)
        # turn
        self._rover.setSpeeds(Speed.D5.value, Speed.R5.value)
        time.sleep(0.6)
        # back
        self._rover.setSpeeds(Speed.D5.value, Speed.D5.value)
        time.sleep(0.3)
        self._rover.setSpeeds(Speed.N.value, Speed.N.value)

    def _backAndTurnRight(self) -> None:
        self._alternateAngle = not self._alternateAngle
        # back
        self._rover.setSpeeds(Speed.R5.value, Speed.R5.value)
        time.sleep(0.8)
        # turn
        self._rover.setSpeeds(Speed.D5.value, Speed.R5.value)
        time.sleep(0.35)
        # back
        self._rover.setSpeeds(Speed.R5.value, Speed.R5.value)
        time.sleep(0.3)
        self._rover.setSpeeds(Speed.N.value, Speed.N.value)

    async def startupTask(self, _: web.Application) -> None:
        """runs the contest balloon continuously"""
        def _implement() -> None:
            self._rover.setSpeeds(Speed.D2.value, Speed.D2.value)
            time.sleep(1) # 1s to get the data populated
            self._rover.setSpeeds(Speed.N.value, Speed.N.value)
            while True:
                time.sleep(0.2) # 200 ms
                if not self._enabled:
                    continue
                value = findContestBalloon(self._lidar.data.toJson(), self._alternateAngle)
                print("#######################")
                print(value)
                if isinstance(value, tuple):
                    if Speed.I in value:
                        if self._alternateAngle:
                            self._enabled = False
                            self._backAndExit()
                            continue

                        self._backAndTurnRight()
                        continue

                    speedL, speedR = value
                    print(f"speedL={speedL}, speedR={speedR}")
                    self._rover.setSpeeds(speedL.value, speedR.value)
        asyncio.create_task(asyncRunInThread(_implement))
