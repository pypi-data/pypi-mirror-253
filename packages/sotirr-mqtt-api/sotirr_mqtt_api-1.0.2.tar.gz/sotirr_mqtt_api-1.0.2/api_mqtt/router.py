"""Содержит все классы и структуры данных для работы с роутерами."""
from importlib import import_module
from typing import Iterable, MutableMapping

from .entities import IAsyncRouterCommand, IRouterCommand

TMqttTopic = str

TRouter = MutableMapping[TMqttTopic, IRouterCommand]
TAsyncRouter = MutableMapping[TMqttTopic, IAsyncRouterCommand]


def get_router(modules: Iterable[str]) -> TRouter:
    """Собирает роутеры со всех модулей в один объект.

    Args:
        modules (Iterable[str], optional): Названия модулей. Defaults to settings.MODULES.

    Returns:
        TRouter: Единый роутер для всего сервиса.
    """
    router_glued: TRouter = {}
    module_name: str = __name__.split('.')[0]
    for module in modules:
        router_path: str = f'.{module}.api.api_mqtt.routes'  # FIXME выписать путь до routes как константу или через settings
        router_module: TRouter = import_module(router_path, module_name).router
        router_glued.update(**router_module)
    return router_glued


def get_subscribe_topics(router: TRouter) -> list[TMqttTopic]:
    """Формирует список всех топиков из роутеров модулей на которые нужно подписаться mqtt клиенту.

    Args:
        router (TRouter): Набор маршрутов.

    Returns:
        list[TMqttTopic]: список всех топиков  которые нужно подписаться mqtt клиенту.
    """
    topics: list[TMqttTopic] = []
    for topic in router:
        topics.append(topic)
    return topics
