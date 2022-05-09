from enum import Enum
from typing import Optional
import serial


class InterfaceCmd(Enum):
    Config = 90
    Write = 98

    ISSMode = 2
    IOModeAndSerial = 1
    Baud9600H = 1
    Baud9600L = 55
    IOType = 0

class RovExCmd(Enum):
    Sync = 0

    SpeedL = 49
    SpeedR = 50

    DisableTimeout = 56
    EnableTimeout = 57


class RovEx:
    def __init__(self, com: str) -> None:
        self._ser = serial.Serial(com, 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_TWO)
        self._ser.write([InterfaceCmd.Config.value,
                         InterfaceCmd.ISSMode.value,
                         InterfaceCmd.IOModeAndSerial.value,
                         InterfaceCmd.Baud9600H.value,
                         InterfaceCmd.Baud9600L.value,
                         InterfaceCmd.IOType.value])

    def send(self, cmd: RovExCmd, value: Optional[int] = None) -> None:
        toSend = [InterfaceCmd.Write.value,
                  RovExCmd.Sync.value,
                  cmd.value]
        if value is not None:
            toSend.append(value)

        print(f"send {toSend}")

        self._ser.write(toSend)


class Rover:
    def __init__(self, com: str) -> None:
        self._rovEx = RovEx(com)
        self._rovEx.send(RovExCmd.DisableTimeout)

    def setSpeeds(self, speedL: int, speedR: int) -> None:
        self._rovEx.send(RovExCmd.SpeedL, speedL)
        self._rovEx.send(RovExCmd.SpeedR, 255 - speedR)
