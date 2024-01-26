"""Msg handlers."""
import json
import logging
from typing import Any, Optional, Protocol, TypedDict


from .entities import (
    IMqttMessage,
    RespMsgDict,
    ResponsePayloadDict,
)
from .mqtt_clients import IAsyncMqttMsgSender, IMqttMsgSender
from .router import TAsyncRouter, TRouter


logger = logging.getLogger(__name__)


class IMsgHandler(Protocol):
    """Interface for message handlers."""

    def handle_msg(self, msg: IMqttMessage) -> None:
        """Proceed mqtt message.

        Args:
            msg (IMqttMessage): Mqtt message
        """
        ...


class IAsyncMsgHandler(Protocol):
    """Interface for async message handlers."""

    async def handle_msg(self, msg: IMqttMessage) -> None:
        """Proceed mqtt message.

        Args:
            msg (IMqttMessage): Mqtt message
        """
        ...


class SimpleMsgHandler():
    """Простой обработчик Mqtt сообщений.

    По топику Mqtt сообщения запускает нужную команду роутера.

    Args:
        topic_fabric (TRouter): Фабрика содержащая
        название топиков и команды которые должны их обрабатывать.
    """

    def __init__(self, topic_fabric: TRouter) -> None:
        self.topic_fabric = topic_fabric

    def handle_msg(self, msg: IMqttMessage) -> None:
        """Proceed mqtt message.

        Args:
            msg (IMqttMessage): Mqtt message
        """
        if command := self.topic_fabric.get(msg.topic):
            command(msg.payload)


class AsyncRouterQueueMsgHandler():
    """Асинхронный обработчик сообщений от mqtt."""

    def __init__(self, topic_fabric: TAsyncRouter) -> None:
        self._topic_fabric = topic_fabric

    async def handle_msg(self, msg: IMqttMessage) -> None:
        """Proceed mqtt message.

        Args:
            msg (IMqttMessage): Mqtt message
        """
        if command := self._topic_fabric.get(msg.topic):
            await command(msg.payload)


class RouterMsgHandlerWithResponse():
    """message handlers with error topics and response.

    По mqtt топику получает команду обработки из фабрики команд.
    Запускает ее передав mqtt payload. Если команда вернула результат
    то он отправляется в очередь отправки для публикации в mqtt.

    Если возникло исключение Error то помещает сообщение об ошибке в
    очередь на отправку для публикации в mqtt error_topic.

    Args:
        topic_fabric (TRouter): Фабрика содержащая название топиков и команды которые должны их обрабатывать.
        mqtt_msg_sender (IMqttMsgSender): Публикатор mqtt сообщений.
        service_topics (dict[str, str]): Словарь содержащий сервисные mqtt топики.
    """

    def __init__(
        self,
        topic_fabric: TRouter,
        service_topics: dict[str, str],
        mqtt_msg_sender: IMqttMsgSender,
    ) -> None:
        self._topic_fabric = topic_fabric
        self._error_topic = service_topics['error']
        self._mqtt_msg_sender = mqtt_msg_sender

    def handle_msg(self, msg: IMqttMessage) -> None:
        """Proceed mqtt message.

        Args:
            msg (IMqttMessage): Mqtt message
        """
        logger.debug('Start handle msg %s', msg)
        resp_topic = msg.response_topic
        if run_command := self._topic_fabric.get(msg.topic):
            try:
                resp_payload: Optional[ResponsePayloadDict] = run_command(msg.payload)
            except BaseException as err:
                logger.warning(err)
                resp_topic = self._error_topic
                resp_payload = {
                    'status': 'error',
                    'msg': 'Internal Error Occurred',
                    'data': None,
                }
            if resp_payload and resp_topic:
                resp_msg: RespMsgDict = {
                    'topic': resp_topic,
                    'cor_data': msg.cor_data,
                    'payload': resp_payload,
                    'retain': False,
                }
                self._mqtt_msg_sender(**resp_msg)


class AsyncRouterMsgHandlerWithResponse():
    """Async message handlers with error topics and response."""

    def __init__(
        self,
        topic_fabric: TAsyncRouter,
        service_topics: dict[str, str],
        mqtt_msg_sender: IAsyncMqttMsgSender,
    ) -> None:
        self._topic_fabric = topic_fabric
        self._error_topic = service_topics['error']
        self._mqtt_msg_sender = mqtt_msg_sender

    async def handle_msg(self, msg: IMqttMessage) -> None:
        """Proceed mqtt message.

        Args:
            msg (IMqttMessage): Mqtt message
        """
        logger.debug('Start handle msg %s', msg)
        resp_topic = msg.response_topic
        if run_command := self._topic_fabric.get(msg.topic):
            try:
                resp_payload: Optional[ResponsePayloadDict] = await run_command(msg.payload)
            except BaseException as err:
                logger.warning(err)
                resp_topic = self._error_topic
                resp_payload = ResponsePayloadDict(
                    status='error',
                    msg='Internal Error Occurred',
                    data=None,
                )
            if resp_payload and resp_topic:
                resp_msg: RespMsgDict = {
                    'topic': resp_topic,
                    'cor_data': msg.cor_data,
                    'payload': resp_payload,
                    'retain': False,
                }
                await self._mqtt_msg_sender(**resp_msg)


class CommandInfoDict(TypedDict):
    """Command information.

    command: str    - command name
    data: Any       - data for command.
    """

    command: str
    data: Any


class IExternalCommandHandler(Protocol):
    """Handler for external command."""

    def __call__(self, data: Any) -> None:
        """Run handler.

        Args:
            data (Any): data

        Returns:
            None
        """


class CommandRunner():
    """Execute commands.

    Args:
        commands_fabric (dict[str, IExternalCommandHandler]): fabric with executed command.

    Methods:
        run_command: execute property commands
    """

    def __init__(self, commands_fabric: dict[str, IExternalCommandHandler]) -> None:
        self.commands_fabric = commands_fabric

    def __call__(self, payload: bytes) -> None:
        """Execute property commands.

        Args:
            payload (CommandInfoDict): property commands
        """
        payload_serialized = json.loads(payload)
        command_runnable = self.commands_fabric[payload_serialized['command']]
        command_runnable(payload_serialized['data'])
