"""Main loop."""
import asyncio
from queue import Queue
from typing import NoReturn, Protocol

from .entities import IMqttMessage
from .msg_handlers import IAsyncMsgHandler, IMsgHandler


class IMainLoop(Protocol):
    """Interface for Main loop.

    Args:
        msg_queue (Queue[IMqttMessage]): que for receive message.
        msg_handler (IMsgHandler): Class for proceed message.
    """

    def __init__(self, msg_queue: Queue[IMqttMessage], msg_handler: IMsgHandler) -> None:
        ...

    def start(self) -> None:
        """Start main loop."""


class IAsyncMainLoop(Protocol):
    """Async Interface for Main loop.

    Args:
        msg_queue (asyncio.Queue[IMqttMessage]): que for receive message.
        msg_handler (IAsyncMsgHandler): Class for proceed message.
    """

    msg_queue: asyncio.Queue[IMqttMessage]
    msg_handler: IAsyncMsgHandler

    async def start(self) -> None:
        """Start main loop."""


class MainLoop():
    """Main loop.

    Receive messages from mqtt queue and sends for further processing.

    Args:
        msg_queue (Queue[IMqttMessage]): que for receive message.
        msg_handler (IMsgHandler): Class for proceed message.
    """

    def __init__(self, msg_queue: Queue[IMqttMessage], msg_handler: IMsgHandler) -> None:
        self.msg_queue = msg_queue
        self._msg_handler = msg_handler

    def start(self) -> NoReturn:
        """Start main loop."""
        while True:
            msg = self.msg_queue.get()
            self._msg_handler.handle_msg(msg=msg)


class AsyncMainLoop():
    """Async Main loop.

    Receive messages from mqtt queue and sends for further processing.

    Args:
        msg_queue (asyncio.Queue[IMqttMessage]): queue for receive message.
        msg_handler (IAsyncMsgHandler): Class for proceed message.
    """

    def __init__(
        self,
        msg_queue: asyncio.Queue[IMqttMessage],
        msg_handler: IAsyncMsgHandler,
    ) -> None:
        self.msg_queue = msg_queue
        self.msg_handler = msg_handler

    async def start(self) -> None:
        """Start async main loop."""
        while True:
            msg = await self.msg_queue.get()
            await self.msg_handler.handle_msg(msg=msg)
