"""Mqtt API."""
import asyncio
import json
import logging
from queue import Queue
import threading
from typing import Any, Optional, Protocol, TypedDict

from paho.mqtt.client import Client, MQTTMessage
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes

from .entities import IMqttMessage, MqttMessage, RespMsgDict


logger = logging.getLogger(__name__)


class IMqttMsgSerializer(Protocol):
    """Интерфейс для стерилизатора mqtt сообщений."""

    def __call__(self, mqtt_msg: MQTTMessage) -> IMqttMessage:
        """Сериализует mqtt сообщение.

        mqtt_msg (MQTTMessage) - mqtt сообщение
        """
        ...


class IMqttMsgSender(Protocol):
    """Интерфейс для публикации Mqtt сообщений."""

    def __call__(self, topic: str, payload: Any, retain: bool, cor_data: Optional[str]) -> None:
        """Публикует Mqtt сообщение.

        Args:
            topic: str                  - Mqtt topic.
            cor_data: Optional[str]     - uniq request id.
            payload: Any                - json serializable payload.
            retain: bool                - Если параметр true то сообщение останется в
                                        топике пока его не перезатрет следующие сообщение.
        """
        ...


class IAsyncMqttMsgSender(Protocol):
    """Интерфейс для публикации Mqtt сообщений."""

    async def __call__(self, topic: str, payload: Any, retain: bool, cor_data: Optional[str]) -> None:
        """Публикует Mqtt сообщение.

        Args:
            topic: str                  - Mqtt topic.
            cor_data: Optional[str]     - uniq request id.
            payload: Any                - json serializable payload.
            retain: bool                - Если параметр true то сообщение останется в
                                        топике пока его не перезатрет следующие сообщение.
        """
        ...


class MqttUserdataDict(TypedDict):
    """Additional data for paho mqtt client.

    topics: list[str]                   - list of topics name for subscribe.
    msg_serializer: IMqttMsgSerializer  - Msg serializer
    msg_queue: Queue[MQTTMessage]       - queue for received msg.
    publisher_queue: Queue[Any]         - queue for publishing msg.
    publisher_loop_timeout: float       - timeout for publishing loop.
    """

    topics: list[str]
    msg_serializer: IMqttMsgSerializer
    msg_queue: Queue[MQTTMessage]
    publisher_queue: Queue[Any]
    publisher_loop_timeout: float


class MQTTReceiver(Client):
    """Mqtt receiver client."""

    def on_disconnect(
        self, client: Client, userdata: dict[str, Any], rc: int, properties: Optional[Properties],
    ) -> None:
        """Логирует отключение mqtt клиента."""
        logger.debug('Mqtt client disconnected with code %s', rc)

    def on_connect(
        self, client: Client, userdata: dict[str, Any], flags: Any, rc: int, properties: Optional[Properties] = None,
    ) -> None:
        """Define the connect callback implementation.

        При подключении подписывается на нужные топики.

        Args:
            client (Client):            - the client instance for this callback
            userdata (dict[str, Any]):  - the private user data as set in Client() or userdata_set()
            flags (Any):                - gives the severity of the message
            rc (int):                   - return code
            properties (Optional[Properties], optional): - Дополнительные опции пятой версии Mqtt.
        """
        logger.debug("Connected to mqtt server with result code %s", rc)
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        if topics := userdata.get('topics'):
            for topic in topics:
                self.subscribe(topic)

    def on_message(self, mqttc: Client, userdata: Any, msg: MQTTMessage) -> None:
        """Define the message received callback implementation.

        Serialize payload and put msg to queue for further processing.
        Queue is taken from userdata.

        Args:
            mqttc (Client):                 - the client instance for this callback
            userdata (Any):                 - the private user data as set in Client() or userdata_set()
            msg (MQTTMessage):              - Mqtt message
        """
        logger.debug('Mqtt message has been received: %s', msg.topic + str(msg.payload))
        if msg_queue := userdata.get('msg_queue'):
            serialized_msg = userdata['msg_serializer'](msg)
            msg_queue.put(serialized_msg)


class MqttClient(Client):
    """Mqtt receiver client."""

    def on_disconnect(
        self, client: Client, userdata: dict[str, Any], rc: int, properties: Optional[Properties],
    ) -> None:
        """Логирует отключение mqtt клиента."""
        logger.debug('Mqtt client disconnected with code %s', rc)

    def on_connect(
        self, client: Client, userdata: dict[str, Any], flags: Any, rc: int, properties: Optional[Properties] = None,
    ) -> None:
        """Define the connect callback implementation.

        При подключении подписывается на нужные топики.

        Args:
            client (Client):            - the client instance for this callback
            userdata (dict[str, Any]):  - the private user data as set in Client() or userdata_set()
            flags (Any):                - gives the severity of the message
            rc (int):                   - return code
            properties (Optional[Properties], optional): - Дополнительные опции пятой версии Mqtt.
        """
        logger.debug("Connected to mqtt server with result code %s", rc)
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        if topics := userdata.get('topics'):
            for topic in topics:
                self.subscribe(topic)

    def on_message(self, mqttc: Client, userdata: Any, msg: MQTTMessage) -> None:
        """Define the message received callback implementation.

        Serialize payload and put msg to queue for further processing.
        Queue is taken from userdata.

        Args:
            mqttc (Client):                 - the client instance for this callback
            userdata (Any):                 - the private user data as set in Client() or userdata_set()
            msg (MQTTMessage):              - Mqtt message
        """
        logger.debug('Mqtt message has been received: %s', msg.topic + str(msg.payload))
        if msg_queue := userdata.get('msg_queue'):
            serialized_msg = userdata['msg_serializer'](msg)
            if isinstance(msg_queue, asyncio.Queue):  # FIXME: Грязь. Переделать.
                asyncio.run_coroutine_threadsafe(msg_queue.put(serialized_msg), msg_queue._loop)
            else:
                msg_queue.put(serialized_msg)

    def on_publish(self, mqttc: Client, userdata: Any, mid: str) -> None:
        logger.debug('Mqtt msg %s was publish', mid)

    def publish(self, topic: str, payload: Any, retain: bool, cor_data: Optional[str]) -> None:
        try:
            json.loads(payload)
        except TypeError:
            payload = json.dumps(payload)

        if cor_data:
            properties = Properties(PacketTypes.PUBLISH)
            properties.CorrelationData = cor_data
        else:
            properties = None

        msg_info = super().publish(topic, payload=payload, properties=properties, retain=retain)

        logger.debug(
            'MQTT msg %s has been published to topic "%s". Cor data: %s. Retain %s',
            msg_info.mid, topic, cor_data, retain,
        )

    async def publish_async(self, topic: str, payload: Any, retain: bool, cor_data: Optional[str]) -> None:
        await asyncio.to_thread(self.publish, topic, payload, retain, cor_data)


class MqttRPClient(MqttClient):
    """Mqtt receiver and publisher client.

    Realize publishing in loop from queues.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Add params to standard paho mqtt client init method.

        Added params:
            self._publisher_thread_terminate: bool
            self._publisher_thread: Optional[threading.Thread]
        """
        self._publisher_thread_terminate: bool = False
        self._publisher_thread: Optional[threading.Thread] = None
        super().__init__(*args, **kwargs)

    def publisher_loop_forever(self) -> None:
        """Read publishing queues and publish their messages to mqtt topics in blocking infinity loop."""
        # def publish(self, topic, payload=None, qos=0, retain=False, properties=None):
        resp_queue = self._userdata['publisher_queue']
        while not self._publisher_thread_terminate:
            resp_msg: RespMsgDict = resp_queue.get()
            self.publish(**resp_msg)

    def publisher_loop_start(self) -> None:
        """This is part of the threaded client interface for publisher.

        Call this once to start a new thread for publishing message.
        """
        if self._publisher_thread is not None:
            return

        self._publisher_thread_terminate = False
        self._publisher_thread = threading.Thread(target=self.publisher_loop_forever)
        self._publisher_thread.daemon = True
        self._publisher_thread.start()
        logger.debug('Mqtt publisher thread has been started.')

    def publisher_loop_stop(self) -> None:
        """This is part of the threaded client interface for publisher.

        Call this once to stop the network thread previously created with publisher_loop_start().
        This call will block until the network thread finishes.
        """
        if self._publisher_thread is None:
            return

        self._publisher_thread_terminate = True
        if threading.current_thread() != self._publisher_thread:
            self._publisher_thread.join()
            self._publisher_thread = None
            logger.debug('Mqtt publisher thread has been stopped.')

    def loop_start(self) -> None:
        """Call this once to start a new thread to process network traffic."""
        super().loop_start()
        self.publisher_loop_start()


class PahoMqttMsgSerializer(IMqttMsgSerializer):
    """Сериалайзер для сообщений от paho mqtt клиента."""

    def __call__(self, mqtt_msg: MQTTMessage) -> IMqttMessage:
        """Сериализует mqtt сообщение.

        mqtt_msg (MQTTMessage): - mqtt сообщение
        """
        cor_data: Optional[str] = getattr(mqtt_msg.properties, 'CorrelationData', None)
        resp_topic: str = getattr(mqtt_msg.properties, 'ResponseTopic', None) or f"{mqtt_msg.topic}/response"
        return MqttMessage(
            topic=mqtt_msg.topic,
            payload=mqtt_msg.payload,
            response_topic=resp_topic,
            cor_data=cor_data,
        )


class MqttMsgSenderViaQueue(IMqttMsgSender):
    """Отправляет сообщение по mqtt.

    Помещает сообщение в очередь для отправки.

    Args:
        publisher_queue (Queue[RespMsgDict]): Очередь для отправки сообщения.
    """

    def __init__(self, publisher_queue: Queue[RespMsgDict]) -> None:
        self._publisher_queue = publisher_queue

    def __call__(self, topic: str, payload: Any, retain: bool, cor_data: Optional[str]) -> None:
        """Публикует Mqtt сообщение.

        Args:
            topic: str                  - Mqtt topic.
            cor_data: Optional[str]     - uniq request id.
            payload: Any                - json serializable payload.
            retain: bool                - Если параметр true то сообщение останется в
                                        топике пока его не перезатрет следующие сообщение.
        """
        pub_msg: RespMsgDict = {
            'topic': topic,
            'cor_data': cor_data,
            'retain': retain,
            'payload': payload,
        }
        self._publisher_queue.put(pub_msg)


def send_to_mqtt(
    topic: str,
    payload: Any,
    retain: bool,
    cor_data: Optional[str],
    publisher_queue: Queue[RespMsgDict],
) -> None:
    """Помещает сообщение mqtt в очередь для отправки.

    Args:
        topic (str):    Топик для отправки
        payload (Any):  Полезная нагрузка
        retain (bool):  Оставлять ли сообщения в топике постоянно.
        cor_data (Optional[str]): Идентификационные данные получателя.
        publisher_queue (Queue[RespMsgDict]): Очередь для отправки сообщения.
    """
    pub_msg: RespMsgDict = {
        'topic': topic,
        'cor_data': cor_data,
        'retain': retain,
        'payload': payload,
    }
    publisher_queue.put(pub_msg)
