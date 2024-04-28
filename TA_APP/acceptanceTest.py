import unittest
from TA_Scheduling.wsgi import *
from django.test import Client
from TA_APP.models import User
from TA_APP.models import Course
from django.core.exceptions import ObjectDoesNotExist


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
    def setUp(self):
        self.user = User(username="newestuser", password="newestuser2")
        self.user.save()
        self.client = Client()

    def test_deleteaccount(self):

        response = self.client.post('/homepage/', {"username": "newestuser", "password": "newestuser2", "status": "delete"})


        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(username="newestuser")




    def test_invaliddeletion(self):

        response = self.client.post('/homepage/', {"username": "newestuser10", "password": "42", "status": "delete"})

        self.assertEqual(response.content, "User does not exist to be deleted")


class SupervisorCreateCourseTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def createCourse(self):
        response = self.client.post('/homepage/', {"course_name": "Chemistry 101", "course_term": "F", "status": "create_course"})

        course = Course.objects.get(course_name="Chemistry 101")

        self.assertEqual(course.course_term, "F")

        course.delete()

    def invalidCoursecreation(self):
        response = self.client.post('/homepage/', {"course_name":"", "status":"create_course"})

        self.assertEqual(response.content, "Missing fields for course creation")


class SupervisorDeleteCourseTest(unittest.TestCase):
    def __init__(self):
        self.client = Client()


class SupervisorAssignUserToCourseTest(unittest.TestCase):
    def __init__(self):
        self.client = Client()
