# python-2gis

A Python library for accessing the 2gis API (http://api.2gis.ru).

## Versioning and API stability

API stability isn't guaranteed before **1.3** version. Library version always will match 2GIS API version.

## Usage

### Development mode

Because 2GIS allows only 1000 requests per month for testing, library allows to cache results of queries.
You are disallowed to use cache in real-life projects, see [agreement](http://api.2gis.ru/about/rules/).

### Example

    import dgis

    client = dgis.API('client-API-key')

    print client.project_list()
    print client.city_list(project_id=11)

## Contributing

If you want to contribute, follow the [pep8](http://www.python.org/dev/peps/pep-0008/) guideline, and include the tests.
