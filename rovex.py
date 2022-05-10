# -*- coding: utf-8 -*-
"""curiousLiDAR Rover Com"""
__copyright__ = ("Copyright (c) 2022 David Dias Horta, Paul Meier")

from enum import Enum
from typing import Optional
import serial # type: ignore


class InterfaceCmd(Enum):
    """usb to serial interface commands"""
    Config = 90
    Write = 98
    Read = 98

    ISSMode = 2
    IOModeAndSerial = 1
    Baud9600H = 1
    Baud9600L = 55
    IOType = 0


class RovExMode(Enum):
    """rover modes"""
    Individual = 0
    IndividualSigned = 1
    Sync = 2
    SyncSigned = 3


class RovExCmd(Enum):
    """rover commands"""
    Sync = 0

    GetSpeedL = 33
    GetSpeedR = 34
    GetEncoder1 = 35
    GetEncoder2 = 36
    GetEncoderS = 37
    GetVolts = 38
    GetCurrent1 = 39
    GetCurrent2 = 40
    GetVersion = 41
    GetAcceleration = 42
    GetMode = 43
    GetVI = 44

    SetSpeedL = 49
    SetSpeedR = 50
    SetTurn = 50
    SetAcceleration = 51
    SetMode = 52

    ResetEncoders = 53

    DisableRegulator = 54
    EnableRegulator = 55

    DisableTimeout = 56
    EnableTimeout = 57


class RovEx:
    """Rover Executor; executes commands on the rover"""
    def __init__(self, com: str) -> None:
        self._ser = serial.Serial(com,
                                  9600,
                                  serial.EIGHTBITS,
                                  serial.PARITY_NONE,
                                  serial.STOPBITS_TWO)
        self._ser.write([InterfaceCmd.Config.value,
                         InterfaceCmd.ISSMode.value,
                         InterfaceCmd.IOModeAndSerial.value,
                         InterfaceCmd.Baud9600H.value,
                         InterfaceCmd.Baud9600L.value,
                         InterfaceCmd.IOType.value])

    def read(self, cmd: RovExCmd) -> bytes:
        """reads the commands response"""
        return self.send(cmd)

    def send(self, cmd: RovExCmd, value: Optional[int] = None) -> bytes:
        """sends the specified command (and optionally the value)"""
        toSend = [InterfaceCmd.Write.value,
                  RovExCmd.Sync.value,
                  cmd.value]
        if value is not None:
            toSend.append(value)

        print(f"send {toSend}")

        self._ser.write(toSend)
        ack, txCount, rxCount = self._ser.read(3)

        print(f"ack={ack} txc={txCount} rxc={rxCount}")

        return self._ser.read(rxCount) # type: ignore


class Rover:
    """Rover handler/wrapper"""
    def __init__(self, com: str) -> None:
        self._rovEx = RovEx(com)
        self._rovEx.send(RovExCmd.DisableTimeout)
        self._rovEx.send(RovExCmd.DisableTimeout)

        print(self._rovEx.send(RovExCmd.GetVersion))
        print(self._rovEx.send(RovExCmd.GetVI))

    def setSpeeds(self, speedL: int, speedR: int) -> None:
        """sets the rover's speeds individually"""
        self._rovEx.send(RovExCmd.SetSpeedL, min(speedL + 1, 255))
        self._rovEx.send(RovExCmd.SetSpeedR, 255 - speedR)
