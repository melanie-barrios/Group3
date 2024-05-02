import unittest
from TA_Scheduling.wsgi import *
from django.test import Client
from TA_APP.models import User
from TA_APP.models import Course
from django.core.exceptions import ObjectDoesNotExist





"""
PBI: As a user I would like to be able to sign into my account so that I can access it securely
"""
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








"""
PBI: As a supervisor I would like to create accounts for staff so that I can assign their responsibilities
"""

class SupervisorCreateAccountTest(unittest.TestCase):
    def __init__(self):
        self.client = Client()



"""
PBI: As a supervisor I would like to delete accounts for staff so that I can delete accounts of individuals who do not work at the school anymore
"""
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



"""
PBI: As a supervisor I would like to create courses for staff so that I can designate them to their respective class to teach
"""

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
    def setUp(self):
        self.Course = Course(course_name="Chemistry 101")
        self.Course.save()
        self.client = Client()

    def validCourseDeletion(self):
        response = self.client.post('/homepage/',{"course_name": "Chemistry 101", "status": "delete_course"})

        with self.assertRaises(ObjectDoesNotExist):
            Course.objects.get(course_name="newestuser")


    def invalidCourseDeletion(self):
        response = self.client.post('/homepage/', {"course_name": "SuperFunClass 101", "status": "delete_course"})

        self.assertEqual(response.content, "User does not exist to be deleted")


class SupervisorEditCourseTest(unittest.TestCase):
    def setUp(self):
        self.Course = Course(course_name="Chemistry 101")
        self.Course.save()
        self.client = Client()

    def validCourseEdit(self):
        response = self.client.post('/homepage/', {"course_name": "Chemistry 101", "editdata":{"course_name": "Chemistry 102"}, "status": "edit_course"})

        with self.assertRaises(ObjectDoesNotExist):
            Course.objects.get(course_name="Chemistry 101")

    def invalidCourseEdit(self):

        response = self.client.post('/homepage/', {"course_name": "Chemistry 102", "editdata": {"course_name": "Chemistry 103"}, "status": "edit_course"})

        self.assertEqual(response.content, "Course does not exist to be edited")



"""
PBI: As a supervisor I would like to assign users to courses so that the proper faculty and registered students are enrolled
"""
class SupervisorAssignUserToCourseTest(unittest.TestCase):
    def __init__(self):
        self.client = Client()
