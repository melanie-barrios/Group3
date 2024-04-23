import unittest

from django.test import Client
from models import User


class LoginTest(unittest.TestCase):
    def setup(self):
        User(email="admin", password="password", username="TheAdmin").save()
        self.client = Client()


    def test_validLogin(self):
        response = self.client.post(' ', {'username': 'TheAdmin', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Successfully logged in')

    def test_invalidLogin(self):
        response = self.client.post(' ', {'username': 'invalidname', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Invalid login')


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
