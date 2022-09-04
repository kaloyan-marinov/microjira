import json
import os
import unittest

os.environ["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

from application import app


class ApplicationTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_1_health_check(self):
        # Act.
        rv = self.client.get(
            "api/health-check",
        )

        body_str = rv.get_data(as_text=True)
        body = json.loads(body_str)

        # Assert.
        assert rv.status_code == 200
        assert body == {
            "health-check": "passed",
        }

    # def test_2_get_projects(self):
    #     # Act.
    #     rv = self.client.get(
    #         "api/projects",
    #     )

    #     body_str = rv.get_data(as_text=True)
    #     body = json.loads(body_str)

    #     # Assert
    #     assert rv.status_code == 200
    #     assert body == {
    #         "projects": [],
    #     }

    # def test_3_create_project(self):
    #     # Arrange.
    #     data_str = json.dumps(
    #         {
    #             "no-key-called-name": "this-value-is-irrelevant",
    #         }
    #     )
    #     headers = {
    #         "Content-Type": "application/json",
    #     }

    #     # Act.
    #     rv = self.client.post(
    #         "api/projects",
    #         data=data_str,
    #         headers=headers,
    #     )

    #     body_str = rv.get_data(as_text=True)
    #     body = json.loads(body_str)

    #     # Assert.
    #     assert rv.status_code == 400
    #     assert body == {
    #         "message": "Your request body must contain a 'name' key",
    #     }

    # def test_4_create_project(self):
    #     # Arrange.
    #     data_str = json.dumps(
    #         {
    #             "name": "Build a basic web application using Flask",
    #         }
    #     )
    #     headers = {
    #         "Content-Type": "application/json",
    #     }

    #     # Act.
    #     rv = self.client.post(
    #         "api/projects",
    #         data=data_str,
    #         headers=headers,
    #     )

    #     body_str = rv.get_data(as_text=True)
    #     body = json.loads(body_str)

    #     # Assert.
    #     assert rv.status_code == 201
    #     assert body == {
    #         "id": 1,
    #         "name": "Build a basic web application using Flask",
    #     }

    #     project_id = body["id"]
    #     project = Project.query.get(project_id)
    #     assert (
    #         repr(project)
    #         == "<Project (id=1, name=Build a basic web application using Flask)>"
    #     )
