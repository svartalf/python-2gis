Search in rubric
===================

Documentation: http://api.2gis.ru/doc/firms/searches/searchinrubric/

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
-----------

Search for firms and rubric: ::

    api.search(what=u'Окна', where=u'Иркутск')
