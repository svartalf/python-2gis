from tests import BaseTestCase


class ListsCase(BaseTestCase):
    """Projects and cities lists test"""

    def test_project_list(self):
        response = self.api.project_list()
        project = response['result'][0]

        self.assertGreater(response['total'], 0)

        self.assertIn('id', project)
        self.assertIn('name', project)

    def test_rubricator(self):
        response = self.api.rubricator()

        self.assertGreater(response['total'], 0)
