# -*- coding: utf-8 -*-
"""asyncThread.py"""
__copyright__ = ("Copyright (c) 2022 David Dias Horta")

from typing import Any, Iterable
from threading import Thread
import asyncio
from queue import Queue


async def asyncRunInThread(target: Any, *args: Iterable[Any]) -> None:
    """runs a function in an awaitable thread"""
    thread = Thread(target = target, args = args)
    thread.start()
    while thread.is_alive():
        await asyncio.sleep(1)

async def asyncRunInThreadWithReturn(target: Any, *args: Iterable[Any]) -> Any:
    """runs a function in an awaitable thread and returns its return value"""
    queue: Queue[Any] = Queue()

    def _implement() -> None:
        ret = target(*args) if args else target()
        queue.put_nowait(ret)

    thread = Thread(target = _implement)
    thread.start()
    while thread.is_alive():
        await asyncio.sleep(1)
    return queue.get_nowait()
