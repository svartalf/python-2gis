# -*- coding: utf-8 _-*-


from dgis.binder import bind_api


__version__ = '1.3.1'


class API(object):
    """2GIS API"""

    def __init__(self, key, host='catalog.api.2gis.ru', version='1.3', register_views=True):
        """

        Parameters::
            key : user API key
            host : base URL for queries
            version : API version for working
            register_views : send information to stats server about a firm profile viewing
        """

        self.key = key
        self.host = host
        self.version = version
        self.register_views = register_views

    """Projects lists

    http://api.2gis.ru/doc/firms/list/project-list/
    """
    project_list = bind_api(
        path='/project/list',
        allowed_param=[],
    )

    """List of the project cities

    http://api.2gis.ru/doc/firms/list/city-list/
    """
    city_list = bind_api(
        path='/city/list',
        allowed_param=['where', 'project_id']
    )

    def rubricator(self, **kwargs):
        """Rubrics search

        http://api.2gis.ru/doc/firms/list/rubricator/
        """

        # `show_children' parameter must be an integer
        kwargs['show_children'] = int(kwargs.pop('show_children', False))

        return self._rubricator(**kwargs)

    _rubricator = bind_api(
        path='/rubricator',
        allowed_param=['where', 'id', 'parent_id', 'show_children', 'sort'],
    )

    def search(self, **kwargs):
        """Firms search

        http://api.2gis.ru/doc/firms/searches/search/
        """

        point = kwargs.pop('point', False)
        if point:
            kwargs['point'] = '%s,%s' % (point[0], point[1])

        bound = kwargs.pop('bound', False)
        if bound:
            kwargs['bound[point1]'] = bound[0]
            kwargs['bound[point2]'] = bound[1]

        filters = kwargs.pop('filters', False)
        if filters:
            for k, v in filters.items():
                kwargs['filters[%s]' % k] = v

        return self._search(**kwargs)

    _search = bind_api(
        path='/search',
        allowed_param=['what', 'where', 'point', 'radius', 'bound', 'page', 'pagesize', 'sort', 'filters'],
    )

    def search_in_rubric(self, **kwargs):
        """Firms search in rubric

        http://api.2gis.ru/doc/firms/searches/searchinrubric/
        """

        point = kwargs.pop('point', False)
        if point:
            kwargs['point'] = '%s,%s' % point

        bound = kwargs.pop('bound', False)
        if bound:
            kwargs['bound[point1]'] = bound[0]
            kwargs['bound[point2]'] = bound[1]

        filters = kwargs.pop('filters', False)
        if filters:
            for k, v in filters.items():
                kwargs['filters[%s]' % k] = v

        return self._search_in_rubric(**kwargs)

    _search_in_rubric = bind_api(
        path='/searchinrubric',
        allowed_param=['what', 'where', 'point', 'radius', 'bound', 'page', 'pagesize', 'sort', 'filters'],
    )

    """Firm filials

    http://api.2gis.ru/doc/firms/searches/firmsbyfilialid/
    """
    firms_by_filial_id = bind_api(
        path='/firmsByFilialId',
        allowed_param=['firmid', 'page' 'pagesize'],
    )

    """Adverts search

    http://api.2gis.ru/doc/firms/searches/adssearch/
    """
    ads_search = bind_api(
        path='/ads/search',
        allowed_param=['what', 'where', 'format', 'page', 'pagesize'],
    )

    """Firm profile

    http://api.2gis.ru/doc/firms/profiles/profile/
    """
    profile = bind_api(
        path='/profile',
        allowed_param=['id', 'hash'],
        register_views=True,
    )

    def geo_search(self, **kwargs):
        """Geo search

        http://api.2gis.ru/doc/geo/search/
        """

        if 'types' in kwargs:
            kwargs['types'] = ','.join(kwargs['types'])

        bound = kwargs.pop('bound', False)
        if bound:
            kwargs['bound[point1]'] = bound[0]
            kwargs['bound[point2]'] = bound[1]

        return self._geo_search(**kwargs)

    _geo_search = bind_api(
        path='/geo/search',
        allowed_param=['q', 'types', 'radius', 'limit', 'project', 'bound', 'format'],
    )

    """Information about a geo object"""
    geo_get = bind_api(
        path='/geo/search',
        allowed_param=['id', ],
    )
