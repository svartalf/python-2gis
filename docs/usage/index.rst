Usage
========

Using a 2GIS API is very simple.

Begin with importing ``dgis`` module ::

    >>> import dgis

Create an API object and give to it your unique API key

    >>> api = dgis.API('1234567890')

You can call all the 2GIS API methods like this

    >>> projects = api.project_list()

Now, ``projects`` is a big list with all available `projects <http://api.2gis.ru/doc/firms/list/project-list/>`_.

All parameters for 2GIS API endpoints are passed as an keyword arguments to the respective library' methods ::

    >>> cities = api.city_list(project_id=11)

You should not pass parameters ``output``, ``callback``, ``key`` and ``version`` to all the methods, library do this internally.
