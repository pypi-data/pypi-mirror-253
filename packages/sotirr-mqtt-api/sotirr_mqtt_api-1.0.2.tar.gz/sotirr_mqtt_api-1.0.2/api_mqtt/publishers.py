"""Содержит все классы и функции связанные mqtt publisher'ом.

Mqtt publisher отслеживает заданные события и отправляет на их основе сообщения mqtt.
"""
from dataclasses import dataclass
from importlib import import_module
import logging
from typing import Iterable, Literal, MutableMapping, Protocol, TypedDict

from .exceptions import Error


logger = logging.getLogger(__name__)


TMqttTopic = str
TObserverType = Literal['table', 'file', 'time_interval', 'internal_event']


class IObservedObject(Protocol):
    """Интерфейс для наблюдаемого объекта.

    На данный момент поддерживаются только файлы и таблицы бд.
    Итоговый объект должен быть хэшируемым.

    type (Literal['table', 'file']): - Тип наблюдаемого объекта.
    value (str)                      - Значение.
    """
    type: TObserverType
    value: str


class IPublisherCommand(Protocol):
    """Интерфейс для публикации mqtt сообщения.

    Methods:
        __call__: Отправляет сообщение на публикацию.
    """

    def __call__(self, publisher_topic: TMqttTopic) -> None:
        """Отправляет сообщение на публикацию в заданный топик.

        Args:
            publisher_topic (str): Mqtt топик в который сообщение будет опубликовано.
        """
        ...


TPublishRouter = MutableMapping[IObservedObject, list[tuple[IPublisherCommand, TMqttTopic]]]


@dataclass(frozen=True)
class ObserverObject(IObservedObject):
    """Наблюдаемый объекта.

    На данный момент поддерживаются только файлы и таблицы бд.

    type (Literal['table', 'file']): - Тип наблюдаемого объекта.
    value (str)                      - Значение.
    """
    type: TObserverType
    value: str


class PublisherRouteDict(TypedDict):
    """Параметры маршрута mqtt publisher'а.

    name (str): - Имя маршрута.
    topic (str): - Mqtt топик для отправки.
    observed_object (IObservedObject): - Наблюдаемый объект.
    publisher (IPublisherCommand): - Команда по формированию и отправке Mqtt сообщения.
    startup (bool): - Если true то первое сообщение формируется и отправляется при старте сервиса.
    """

    name: str
    topic: str
    observed_object: IObservedObject
    publisher: IPublisherCommand
    startup: bool


class EventCallback:
    """Обратный вызов для сработавшего события."""

    def __init__(self, publish_router: TPublishRouter) -> None:
        self.publish_router = publish_router

    def __call__(self, observed_obj: ObserverObject) -> None:
        """Hook executed after observed event ocurred.

        Args:
            observed_obj (ObserverObject): Наблюдаемый объект.
        """
        for publisher, topic in self.publish_router.get(observed_obj, [(lambda *args: None, 'empty')]):
            if publisher and topic:
                try:
                    publisher(topic)
                except Error as err:
                    logger.error('An error occurred while generating a message to send. %s %s', err.message, err.data)


def get_publish_routes(modules: Iterable[str]) -> list[PublisherRouteDict]:
    """Собирает маршруты отправки сообщений со всех модулей в один объект.

    Args:
        modules (Iterable[str], optional): Названия модулей.

    Returns:
        list[PublisherRouteDict]: Единый список маршрутов на отправку для всего сервиса.
    """
    publish_routes_glued: list[PublisherRouteDict] = []
    module_name: str = __name__.split('.')[0]
    for module in modules:
        router_path: str = f'.{module}.api.api_mqtt.publishers'  # FIXME выписать путь до routes как константу или через settings
        publish_routes_from_module = import_module(router_path, module_name).publish_routes
        publish_routes_glued.extend(publish_routes_from_module)
    return publish_routes_glued


class PublishRouterBuilder:
    """Формирует маршрутизатор для mqtt publisher'a."""

    def __call__(self, publish_routes: list[PublisherRouteDict]) -> TPublishRouter:
        """Формирует маршрутизатор для mqtt publisher'a.

        Args:
            publish_routes (list[PublisherRouteDict]): Список маршрутов на отправку.

        Returns:
            TPublishRouter: Маршрутизатор для mqtt publisher'a.
        """
        router: TPublishRouter = {}
        for route in publish_routes:
            if route['observed_object'] not in router:
                router[route['observed_object']] = []
            router[route['observed_object']].append((route['publisher'], route['topic']))
        return router


def run_startup_publisher(publish_routes: list[PublisherRouteDict]) -> None:
    """Отправляет mqtt сообщения при старте системы на основании маршрутов mqtt publisher'a.

    Args:
        publish_routes (list[PublisherRouteDict]): _description_
    """
    for route in publish_routes:
        if route['startup']:
            try:
                route['publisher'](route['topic'])
            except Error as err:
                logger.error('An error occurred while generating a message to send. %s %s', err.message, err.data)
