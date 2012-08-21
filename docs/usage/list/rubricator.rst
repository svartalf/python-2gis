Rubricator
=============

Documentation: http://api.2gis.ru/doc/firms/list/rubricator/

Allowed parameters:

 * where
 * id
 * parent_id
 * show_children
 * sort

Examples
----------

All rubrics related to the city: ::

    api.rubricator(where=u'Новосибирск')

Get information about a one rubric: ::

    api.rubricator(id=1234567890)

Get all child rubrics: ::

    api.rubricator(parent_id=1234567890)

Get rubric with all the children ::

    api.rubricator(id=1234567890, show_children=True)

