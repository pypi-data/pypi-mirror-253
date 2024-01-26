"""Сущности и интерфейсы matt api."""
from dataclasses import dataclass
from typing import Any, Literal, Optional, Protocol, TypedDict


class IMqttMessage(Protocol):
    """Интерфейс для mqtt сообщения.

    topic: str                      - Mqtt топик на который пришло сообщение.
    cor_data: Optional[str]         - Идентификатор для сообщения ответа.
    payload: Any                    - Полезная нагрузка сообщения.
    response_topic: Optional[str]   - Mqtt топик на который ожидается ответ.
    """

    topic: str
    payload: bytes
    response_topic: Optional[str]
    cor_data: Optional[str]


@dataclass
class MqttMessage:
    """Mqtt сообщение.

    topic (str)                 - Mqtt топик на который пришло сообщение.
    payload (bytes)             - Полезная нагрузка сообщения.
    response_topic (str)        - Mqtt топик на который ожидается ответ.
    cor_data (Optional[str])    - Идентификатор для сообщения ответа.
    """

    topic: str
    payload: bytes
    response_topic: Optional[str]
    cor_data: Optional[str]


class RespMsgDict(TypedDict):
    """Response msg dict.

    topic: str                  - response topic.
    cor_data: Optional[str]     - uniq request id.
    payload: Any                - json serializable payload.
    retain: bool                - Если параметр true то сообщение останется в
                                топике пока его не перезатрет следующие сообщение.
    """

    topic: str
    cor_data: Optional[str]
    payload: Any
    retain: bool


class ResponsePayloadDict(TypedDict):
    """Формат для полезной нагрузки в ответе mqtt."""

    status: Literal['success', 'error']
    msg: str
    data: Any


class IRouterCommand(Protocol):
    """Interface for router command.

    Methods:
        __call__: Run command. Return Any.
    """

    def __call__(self, payload: bytes) -> Optional[ResponsePayloadDict]:
        """Run command.

        payload (bytes) - Полезная нагрузка mqtt сообщения.
        """


class IAsyncRouterCommand(Protocol):
    """Interface for router command.

    Methods:
        __call__: Run command. Return Any.
    """

    async def __call__(self, payload: bytes) -> Optional[ResponsePayloadDict]:
        """Run command.

        payload (bytes) - Полезная нагрузка mqtt сообщения.
        """
