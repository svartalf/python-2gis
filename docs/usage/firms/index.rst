Firms search
==============

Documentation: http://api.2gis.ru/doc/firms/searches/search/

Allowed parameters:

 * what
 * where
 * point : list of two coordinates [lon, lat]
 * radius
 * bound : [[lon1, lat1], [lon2, lat2]]
 * page
 * pagesize
 * sort
 * filters

Examples
---------

Search for firms and rubrics: ::

    api.search(what=u'пиво', where=u'Иркутск')

Search for firms and rubrics in radius of 1000 m from a point: ::

    api.search(what=u'пиво', point=[104.281352, 52.287771], radius=1000)

Search for firms and rubrics in a bounds: ::

    api.search(what=u'пиво', bound=[[82.801886, 54.991984], [82.9019, 52.9910]])

Search with worktime filter: ::

    filters = {
        'worktime': 'mon,23:01',
    }
    api.search(what=u'пиво', where=u'Иркутск', filters=filters)
