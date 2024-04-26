import unittest
from TA_Scheduling.wsgi import *
from django.test import Client
from TA_APP.models import User


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.user = User(username="newestuser", password="newestuser2")
        self.user.save()
        self.client = Client()


    def test_validLogin(self):

        response = self.client.post("/", {"username": "newestuser", "password": "newestuser2"})
        ##routes to homepage if valid
        self.assertEqual(response.url, "/homepage/")

        self.user.delete()

    def test_invalidLogin(self):

        response = self.client.post("/", {"username": "test_user60", "password": "PASSWORD60"})

        content = response.content.decode('utf-8')

        ##if html contains message that username or password is incorrect creds are invalid
        self.assertIn("Username or password is incorrect", content, "Login credentials are invalid")

        self.user.delete()










class SupervisorCreateAccountTest(unittest.TestCase):
    def __init__(self):
        self.client = Client()


class SupervisorDeleteAccountTest(unittest.TestCase):
    def __init__(self):
        self.client = Client()


class SupervisorCreateCourseTest(unittest.TestCase):
    def __init__(self):
        self.client = Client()


class SupervisorDeleteCourseTest(unittest.TestCase):
    def __init__(self):
        self.client = Client()


class SupervisorAssignUserToCourseTest(unittest.TestCase):
    def __init__(self):
        self.client = Client()
