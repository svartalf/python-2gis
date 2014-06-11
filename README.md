# python-2gis

[![Build Status](https://travis-ci.org/irkru/python-2gis.svg?branch=master)](https://travis-ci.org/irkru/python-2gis)

A Python library for accessing the 2gis API (http://api.2gis.ru).

Documentation: http://python-2gis.readthedocs.org

## Versioning and API stability

API stability isn't guaranteed before **1.3** version. Library version always will match 2GIS API version.

## Usage

### Example

    import dgis

    client = dgis.API('client-API-key')

    print client.project_list()
    print client.city_list(project_id=11)

## Contributing

If you want to contribute, follow the [pep8](http://www.python.org/dev/peps/pep-0008/) guideline.
