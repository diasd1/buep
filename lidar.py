# -*- coding: utf-8 -*-
"""curiousLiDAR LiDAR Messages"""
__copyright__ = ("Copyright (c) 2022 David Dias Horta, Paul Meier")

import math
from enum import Enum
from time import sleep
from typing import List
import asyncio

import serial # type: ignore
from aiohttp import web

from asyncThread import asyncRunInThread

class LiDARMessageState(Enum):
    """enum for the different LiDAR message states"""
    Header = "header"
    TypeAndQuantity = "typeAndQuantity"
    StartAngle = "startAngle"
    EndAngle = "endAngle"
    CheckCode = "checkCode"
    Data = "data"
    Nought = "nought"


class LiDARCurrentData:
    """holds the current data and auto updates flexibly"""
    def __init__(self) -> None:
        self._dist = [ 0.0 for _ in range(360) ]

    def toJson(self) -> List[float]:
        """serialise"""
        return self._dist

    def update(self, data: List[float], startAngle: float, endAngle: float) -> None:
        """updates the current data flexibly"""
        angleRange = abs(endAngle - startAngle)
        for index, dist in enumerate(data):
            angCorrect = 0 if dist == 0.0 else math.atan(21.8 * (155.3 - dist) / (155.3 * dist))

            angle = math.floor(angCorrect + startAngle + angleRange / len(data) * index)
            if angle >= 360:
                angle -= 360

            if dist > 20.0:
                self._dist[angle] = dist


class LiDARMessageHandler:
    """handles LiDAR messages"""
    def __init__(self) -> None:
        self._currentData = LiDARCurrentData()
        self._state = LiDARMessageState.Header
        self._lastByte = 0
        self._byteCount = 0
        self._data: List[float] = [ ]
        self._startAngle = 0.0
        self._endAngle = 0.0
        self._quantity = 0

    @property
    def currentData(self) -> LiDARCurrentData:
        """the current LiDAR data"""
        return self._currentData

    @property
    def _isFirstByte(self) -> bool:
        return self._byteCount == 0

    def handle(self, byte: int) -> None:
        """handles a (partial) LiDAR message"""
        if self._isFirstByte and not self._state == LiDARMessageState.Nought:
            self._byteCount += 1
            self._lastByte = byte
            #print("(LSB)", byte)
            return

        if self._state == LiDARMessageState.Nought and byte == 170:
            self._byteCount += 1
            self._lastByte = byte
            #print("(LSB)", byte)
            self._state = LiDARMessageState.Header
            return

        #print("(MSB)", byte)
        self._byteCount = 0

        if self._state == LiDARMessageState.Header:
            if self._lastByte == 170 and byte == 85:
                self._state = LiDARMessageState.TypeAndQuantity
        elif self._state == LiDARMessageState.TypeAndQuantity:
            self._quantity = byte
            #freq = (self._lastByte >> 1) / 10
            #print("freq", freq)
            #print("type", self._lastByte & 1)
            self._state = LiDARMessageState.StartAngle
        elif self._state == LiDARMessageState.StartAngle:
            self._startAngle = ((self._lastByte + byte * 255) >> 1) / 64
            self._state = LiDARMessageState.EndAngle
        elif self._state == LiDARMessageState.EndAngle:
            self._endAngle = ((self._lastByte + byte * 255) >> 1) / 64
            self._state = LiDARMessageState.CheckCode
        elif self._state == LiDARMessageState.CheckCode:
            self._state = LiDARMessageState.Data
        elif self._state == LiDARMessageState.Data:
            self._data.append((self._lastByte + byte * 255) / 4)
            if len(self._data) >= self._quantity:
                self._currentData.update(self._data, self._startAngle, self._endAngle)
                self._data = [ ]
                self._state = LiDARMessageState.Nought

        self._lastByte = byte


class LiDAR:
    """handles the LiDAR connection"""
    def __init__(self, com: str) -> None:
        self._com = com
        self._handler = LiDARMessageHandler()

    @property
    def data(self) -> LiDARCurrentData:
        """the current LiDAR data"""
        return self._handler.currentData

    async def startupTask(self, _: web.Application) -> None:
        """
        returns a startup task for the aiohttp webserver

        this startup task will continuously handle ann LiDAR communication
        """
        def _implement() -> None:
            while True:
                try:
                    ser = serial.Serial(self._com, 115200)

                    while True:
                        self._handler.handle(int.from_bytes(ser.read(), "big"))
                except Exception as exc:
                    print(exc)
                    sleep(1)
        asyncio.create_task(asyncRunInThread(_implement))
