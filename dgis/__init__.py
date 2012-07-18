# -*- coding: utf-8 _-*-


from dgis.binder import bind_api


class API(object):
    """API ДубльГИС"""

    def __init__(self, key, host='catalog.api.2gis.ru', version='1.3'):
        """

        Параметры::
            key : уникальный ключ пользователя API
            host : базовый URL для запросов
            version : версия API, с которой идет работа
        """

        self.key = key
        self.host = host
        self.version = version

    """Список проектов

    http://api.2gis.ru/doc/firms/list/project-list/
    """
    project_list = bind_api(
        path='/project/list',
        allowed_param=[],
    )

    """Список городов проекта

    http://api.2gis.ru/doc/firms/list/city-list/
    """
    city_list = bind_api(
        path='/city/list',
        allowed_param=['where', 'project_id']
    )
