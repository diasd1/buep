import math
from enum import Enum
from typing import List

class LiDARMessageState(Enum):
    Header = "header"
    TypeAndQuantity = "typeAndQuantity"
    StartAngle = "startAngle"
    EndAngle = "endAngle"
    CheckCode = "checkCode"
    Data = "data"
    Nought = "nought"


class LiDARCurrentData:
    def __init__(self) -> None:
        self._dist = [ 0.0 for _ in range(360) ]

    def update(self, data: List[float], startAngle, endAngle):
        angleRange = abs(endAngle - startAngle)
        for index, dist in enumerate(data):
            angCorrect = 0 if dist == 0.0 else math.atan(21.8 * (155.3 - dist) / (155.3 * dist))
            
            angle = math.floor(angCorrect + startAngle + angleRange / len(data) * index)
            if angle >= 360:
                angle -= 360
            
            if dist > 20.0:
                self._dist[angle] = dist


class LiDARMessage:
    def __init__(self, data: LiDARCurrentData):
        self._currentData = data
        self._state = LiDARMessageState.Header
        self._lastByte = 0
        self._byteCount = 0
        self._data = [ ]
        self._startAngle = 0.0
        self._endAngle = 0.0
        self._quantity = 0

    @property
    def isFirstByte(self):
        return self._byteCount == 0

    def update(self, byte: int):
        if self.isFirstByte and not self._state == LiDARMessageState.Nought:
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
            freq = (self._lastByte >> 1) / 10
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
            self._dataCount = 0
        elif self._state == LiDARMessageState.Data:
            self._data.append((self._lastByte + byte * 255) / 4)
            if len(self._data) >= self._quantity:
                #print(f"quantity={self._quantity} start={self._startAngle}° end={self._endAngle}° data={self._data}")
                self._currentData.update(self._data, self._startAngle, self._endAngle)
                self._data = [ ]
                self._state = LiDARMessageState.Nought

        self._lastByte = byte
