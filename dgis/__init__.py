# -*- coding: utf-8 _-*-


from dgis.binder import bind_api


__version__ = '0.8'


class API(object):
    """2GIS API"""

    def __init__(self, key, host='catalog.api.2gis.ru', version='1.3', cache=False):
        """

        Parameters::
            key : user API key
            host : base URL for queries
            version : API version for working
            cache : enable cache of the requests
        """

        self.key = key
        self.host = host
        self.version = version
        self.cache = cache

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

    """Rubrics search

    http://api.2gis.ru/doc/firms/list/rubricator/
    """
    rubricator = bind_api(
        path='/rubricator',
        allowed_param=['where', 'id', 'parent_id'],
    )

    """Firms search

    http://api.2gis.ru/doc/firms/searches/search/
    """
    search = bind_api(
        path='/search',
        allowed_param=['what', 'where', 'point', 'radius', 'bound', 'page', 'pagesize', 'sort', 'filters'],
    )

    """Firms search in rubric

    http://api.2gis.ru/doc/firms/searches/searchinrubric/
    """
    search_in_rubric = bind_api(
        path='/searchinrubric',
        allowed_param=['what', 'where', 'point', 'radius', 'bound', 'page', 'pagesize', 'sort', 'filters'],
    )

    """Firm filials

    http://api.2gis.ru/doc/firms/searches/firmsbyfilialid/
    """
    firms_by_filial_id = bind_api(
        path='/firmsByFilialId',
        allowed_param=['firmid', ],
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
    )

    """Geo search

    http://api.2gis.ru/doc/geo/search/
    """
    geo_search = bind_api(
        path='/geo/search',
        allowed_param=['q', 'types', 'radius', 'limit', 'project', 'bound', 'format'],
    )

    # TODO: `types` parameter must be a list or tuple. API must convert it into a string manually
    # TODO: `bound` parameter must be a list of a 4 float values

    """Information about a geo object"""
    geo_get = bind_api(
        path='/geo/search',
        allowed_param=['id', ],
    )
