import asyncio
import logging
from queue import Queue
from typing import Any, Coroutine, NoReturn, Optional

from paho.mqtt.client import Client

from .entities import (
    IMqttMessage,
    RespMsgDict,
)
from .main_loop import (
    AsyncMainLoop,
    MainLoop,
)
from .mqtt_clients import (
    MqttClient,
    MqttMsgSenderViaQueue,
    MqttRPClient,
    MqttUserdataDict,
    PahoMqttMsgSerializer,
)
from .msg_handlers import (
    AsyncRouterMsgHandlerWithResponse,
    RouterMsgHandlerWithResponse,
)
from .router import (
    TAsyncRouter,
    TRouter,
)


logger = logging.getLogger(__name__)


class MqttApiWithSeparatePublishThread():

    def __init__(
        self, router: TRouter, service_topics: dict[str, str], client_id: str, host: str = 'localhost',
        publisher_loop_timeout: float = 0.5,
    ) -> None:
        self._router = router
        self._service_topics = service_topics
        self._client_id = client_id
        self._host = host
        self._publisher_loop_timeout = publisher_loop_timeout

        self._receiver_queue: Queue[IMqttMessage] = Queue()
        self._publisher_queue: Queue[RespMsgDict] = Queue()

        self._msg_sender = MqttMsgSenderViaQueue(self._publisher_queue)

    def run(self) -> NoReturn:
        _receive_msg_serializer = PahoMqttMsgSerializer()
        _userdata: MqttUserdataDict = {
            'topics': list(self._router),
            'msg_serializer': _receive_msg_serializer,
            'msg_queue': self._receiver_queue,
            'publisher_queue': self._publisher_queue,
            'publisher_loop_timeout': self._publisher_loop_timeout,
        }
        _mqtt_client: Client = MqttRPClient(client_id=self._client_id,  protocol=5)
        _mqtt_client.user_data_set(userdata=_userdata)
        _mqtt_client.connect(self._host)
        _mqtt_client.loop_start()

        _msg_handler = RouterMsgHandlerWithResponse(
            self._router,
            self._service_topics,
            self._msg_sender,
            )
        _main_loop = MainLoop(msg_queue=self._receiver_queue, msg_handler=_msg_handler)
        _main_loop.start()

    def publish(self, topic: str, payload: Any, retain: bool, cor_data: Optional[str]) -> None:
        self._msg_sender(topic, payload, retain, cor_data)


class MqttApi():

    def __init__(
        self, router: TRouter, service_topics: dict[str, str], client_id: str, host: str = 'localhost',
    ) -> None:
        self._router = router
        self._service_topics = service_topics
        self._client_id = client_id
        self._host = host

    def run(self) -> NoReturn:

        receiver_queue: Queue[IMqttMessage] = Queue()

        _receive_msg_serializer = PahoMqttMsgSerializer()
        _userdata = {
            'topics': list(self._router),
            'msg_serializer': _receive_msg_serializer,
            'msg_queue': receiver_queue,
        }
        _mqtt_client: Client = MqttClient(client_id=self._client_id,  protocol=5)
        _mqtt_client.user_data_set(userdata=_userdata)
        _mqtt_client.connect(self._host)
        _mqtt_client.loop_start()

        self._msg_sender = _mqtt_client.publish

        _msg_handler = RouterMsgHandlerWithResponse(
            self._router,
            self._service_topics,
            self._msg_sender,
            )
        _main_loop = MainLoop(msg_queue=receiver_queue, msg_handler=_msg_handler)
        _main_loop.start()

    def publish(self, topic: str, payload: Any, retain: bool, cor_data: Optional[str]) -> None:
        if hasattr(self, '_msg_sender'):
            self._msg_sender(topic, payload, retain, cor_data)


class MqttApiAsync():

    def __init__(
        self, router: TAsyncRouter, service_topics: dict[str, str], client_id: str, host: str = 'localhost',
    ) -> None:
        self._router = router
        self._service_topics = service_topics
        self._client_id = client_id
        self._host = host

    def run(self) -> Coroutine[Any, Any, None]:

        receiver_queue: asyncio.Queue[IMqttMessage] = asyncio.Queue()
        _receive_msg_serializer = PahoMqttMsgSerializer()
        _userdata = {
            'topics': list(self._router),
            'msg_serializer': _receive_msg_serializer,
            'msg_queue': receiver_queue,
        }
        _mqtt_client: Client = MqttClient(client_id=self._client_id,  protocol=5)
        _mqtt_client.user_data_set(userdata=_userdata)
        _mqtt_client.connect(self._host)
        _mqtt_client.loop_start()

        self._msg_sender = _mqtt_client.publish_async

        _msg_handler = AsyncRouterMsgHandlerWithResponse(
            self._router,
            self._service_topics,
            self._msg_sender,
            )
        _main_loop = AsyncMainLoop(msg_queue=receiver_queue, msg_handler=_msg_handler)

        return _main_loop.start()

    async def publish(self, topic: str, payload: Any, retain: bool, cor_data: Optional[str] = None) -> None:
        if hasattr(self, '_msg_sender'):
            await self._msg_sender(topic, payload, retain, cor_data)
