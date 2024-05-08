import unittest
from TA_Scheduling.wsgi import *
from django.test import TestCase, Client
from TA_APP.models import User, Course, CourseSection, LabSection
from django.core.exceptions import ObjectDoesNotExist
import TA_APP.functions as functions

"""
PBI: As a user I would like to be able to sign into my account so that I can access it securely
"""


class LoginTest(TestCase):
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


class SupervisorCreateAccountTest(TestCase):
    def setUp(self):
        self.temp = User(name="Test", username="test_user", password="PASSWORD", email="test@uwm.edu",
                         phone_number=1234567890, address="123 1st street", type="S")
        self.temp.save()
        self.client = Client()
        session = self.client.session
        session['username'] = 'test_user'
        session.save()

    def tearDown(self):
        ##self.temp.delete()
        ##User.objects.get(username="test_user4").delete()

    def test_ValidCreateAccount1(self):
        resp = self.client.post('/account-management/',
                                {'name': 'Test4', 'username': 'test_user4', 'password': 'PASSWORD4',
                                 'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street',
                                 "type": "TA", 'skills': '', 'status': 'create'}, follow=True)

        self.assertEqual(resp.context['message'], "Account Created Successfully",
                         msg="Message for successful account creation failed")

    def test_ValidCreateAccount2(self):
        resp = self.client.post('/account-management/',
                                {'name': 'Test4', 'username': 'test_user4', 'password': 'PASSWORD4',
                                 'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street',
                                 "type": "TA", 'skills': '', 'status': 'create'}, follow=True)


        self.assertEqual("test_user4", User.objects.get(username="test_user4").username,
                         msg="Account should be present in the database.")

    def test_InvalidCreateAccount1(self):
        resp = self.client.post('/account-management/',
                                {'name': 'Test4', 'username': 'test_user', 'password': 'PASSWORD4',
                                 'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street',
                                 "type": "TA", 'skills': '', 'status': 'create'}, follow=True)

        print(resp.context['message'])

        self.assertEqual(resp.context['message'], "Duplicate username or missing form field",
                         msg="Message for duplicate account creation failed")

    def test_InvalidCreateAccount2(self):
        resp = self.client.post('account-management/',
                                {'name': 'Test4', 'username': '', 'password': 'PASSWORD4',
                                 'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street',
                                 "type": "TA", 'skills': '', 'status': 'create'}, follow=True)
        self.assertEqual(resp.context['message'], "Duplicate username or missing form field",
                         msg="Message for missing field account creation failed")


"""
PBI: As a supervisor I would like to delete accounts for staff so that I can delete accounts of individuals who do not work at the school anymore
"""


class SupervisorDeleteAccountTest(TestCase):
    def setUp(self):
        self.user = User(username="newestuser", password="newestuser2")
        self.user.save()
        self.client = Client()

    def test_deleteaccount(self):
        response = self.client.post('/homepage/',
                                    {"username": "newestuser", "password": "newestuser2", "status": "delete"})

        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(username="newestuser")

    def test_invaliddeletion(self):
        response = self.client.post('/homepage/', {"username": "newestuser10", "password": "42", "status": "delete"})

        self.assertEqual(response.content, "User does not exist to be deleted")


"""
PBI: As a supervisor I would like to create courses for staff so that I can designate them to their respective class to teach
"""


class SupervisorCreateCourseTest(TestCase):
    def setUp(self):
        self.client = Client()

    def createCourse(self):
        response = self.client.post('/homepage/',
                                    {"course_name": "Chemistry 101", "course_term": "F", "status": "create_course"})

        course = Course.objects.get(course_name="Chemistry 101")

        self.assertEqual(course.course_term, "F")

        course.delete()

    def invalidCoursecreation(self):
        response = self.client.post('/homepage/', {"course_name": "", "status": "create_course"})

        self.assertEqual(response.content, "Missing fields for course creation")


class SupervisorDeleteCourseTest(TestCase):
    def setUp(self):
        self.Course = Course(course_name="Chemistry 101")
        self.Course.save()
        self.client = Client()

    def validCourseDeletion(self):
        response = self.client.post('/homepage/', {"course_name": "Chemistry 101", "status": "delete_course"})

        with self.assertRaises(ObjectDoesNotExist):
            Course.objects.get(course_name="newestuser")

    def invalidCourseDeletion(self):
        response = self.client.post('/homepage/', {"course_name": "SuperFunClass 101", "status": "delete_course"})

        self.assertEqual(response.content, "User does not exist to be deleted")

    class SupervisorCreateCourseSectionTest(TestCase):
        def setUp(self):
            self.temp = User(name="Test", username="test_user", password="PASSWORD", email="test@uwm.edu",
                             phone_number=1234567890, address="123 1st street", type="S")
            self.temp.save()
            self.temp_course = Course(course_id="CS101", course_name="Test Course", course_term="F")
            self.temp_course.save()
            self.test_courseSection = CourseSection(section_id=4560, section_number=202, course=self.temp_course,
                                                    Time="MW 9:30AM", Location="EMS", credits=3, instructor=self.temp)
            self.test_courseSection.save()
            self.client = Client()
            session = self.client.session
            session['username'] = 'test_user'
            session.save()

        def tearDown(self):
            self.temp.delete()
            self.temp_course.delete()
            self.test_courseSection.delete()

        def test_ValidCreateCourseSection1(self):
            resp = self.client.post('/course-management/',
                                    {"section_id": 456, "section_number": 201, "course": "CS101",
                                     "Time": "MW 9:30AM", "Location": "EMS", "credits": 3,
                                     "status": "create_courseSection"}, follow=True)
            self.assertEqual(resp.context['message'], "Course Section created successfully",
                             msg="Message for successful course section creation failed")

        def test_ValidCreateCourseSection2(self):
            resp = self.client.post('/course-management/',
                                    {"section_id": 456, "section_number": 201, "course": "CS101",
                                     "Time": "MW 9:30AM", "Location": "EMS", "credits": 3,
                                     "status": "create_courseSection"}, follow=True)
            self.assertEqual(201, CourseSection.objects.get(section_number=201).section_number,
                             msg="Message for successful course section creation failed")

        def test_InvalidCreateCourseSection1(self):
            resp = self.client.post('course-management/',
                                    {"section_id": 456, "section_number": '', "course": "CS101",
                                     "Time": "MW 9:30AM", "Location": "EMS", "credits": 3,
                                     "status": "create_courseSection"}, follow=True)
            self.assertEqual(resp.context['message'], "Course section missing a field or is a duplicate",
                             msg="Message for unsuccessful course section creation failed")

        def test_InvalidCreateCourseSection2(self):
            resp = self.client.post('course-management/',
                                    {"section_id": 456, "section_number": 202, "course": "CS101",
                                     "Time": "MW 9:30AM", "Location": "EMS", "credits": 3,
                                     "status": "create_courseSection"}, follow=True)
            self.assertEqual(resp.context['message'], "Course section missing a field or is a duplicate",
                             msg="Message for unsuccessful course section creation failed")

    class SupervisorDeleteCourseSectionTest(TestCase):
        def setUp(self):
            self.temp = User(name="Test", username="test_user", password="PASSWORD", email="test@uwm.edu",
                             phone_number=1234567890, address="123 1st street", type="S")
            self.temp.save()
            self.temp_course = Course(course_id="CS101", course_name="Test Course", course_term="F")
            self.temp_course.save()
            self.test_courseSection = CourseSection(section_id=4560, section_number=202, course=self.temp_course,
                                                    Time="MW 9:30AM", Location="EMS", credits=3, instructor=self.temp)
            self.test_courseSection.save()
            self.client = Client()
            session = self.client.session
            session['username'] = 'test_user'
            session.save()

        def tearDown(self):
            self.temp.delete()
            self.temp_course.delete()
            self.test_courseSection.delete()

        def test_ValidDeleteCourseSection1(self):
            resp = self.client.post('course-management/',
                                    {"section_id": 4560, "status": "delete_courseSection"}, follow=True)
            self.assertEqual(resp.context['message'], "Course Section Deletion successful",
                             msg="Message for successful course section creation failed")

        def test_ValidDeleteCourseSection2(self):
            resp = self.client.post('course-management/',
                                    {"section_id": 4560, "status": "delete_courseSection"}, follow=True)
            self.assertEqual([], functions.CourseSection_func.get(self, "section_id", "4560"),
                             msg="Message for successful course section creation failed")

        def test_InvalidDeleteCourseSection1(self):
            resp = self.client.post('course-management/',
                                    {"section_id": 45600, "status": "delete_courseSection"}, follow=True)
            self.assertEqual(resp.context['message'], "Course section does not exist",
                             msg="Message for successful course section creation failed")

    class SupervisorCreateLabSectionTest(TestCase):
        def setUp(self):
            self.temp3 = User(name="Test3", username="test_user3", password="PASSWORD3", email="test3@uwm.edu",
                              phone_number=1234567894, address="222 1st street", type="TA")
            self.temp_course = Course(course_id="CS303", course_name="Test Course", course_term="F")
            self.test_courseSection = CourseSection(section_id=123, section_number=303, course=self.temp_course,
                                                    Time="MW 9:30AM", Location="EMS", credits=3, instructor=self.temp2)
            self.test_lab_section = LabSection(section_id=222, section_number=302,
                                               course_section=self.test_courseSection,
                                               course=self.temp_course, Time="MW 9:30AM", Location="EMS",
                                               Type="L", ta=self.temp3)
            self.temp3.save()
            self.temp_course.save()
            self.test_courseSection.save()
            self.test_lab_section.save()
            self.client = Client()
            session = self.client.session
            session['username'] = 'test_user'
            session.save()

        def tearDown(self):
            self.temp3.delete()
            self.temp_course.delete()
            self.test_courseSection.delete()
            self.test_lab_section.delete()

        def test_ValidCreateCourseSection1(self):
            resp = self.client.post('course-management/',
                                    {"section_id": 222, "section_number": 301,
                                     "course_section": 303,
                                     "course": "CS303", "Time": "MW 9:30AM", "Location": "EMS",
                                     "Type": "L", "status": "create_LabSection"}, follow=True)
            self.assertEqual(resp.context['message'], "Lab Section created successfully",
                             msg="Message for successful course section creation failed")

        def test_ValidCreateCourseSection2(self):
            resp = self.client.post('course-management/',
                                    {"section_id": 222, "section_number": 301,
                                     "course_section": 303,
                                     "course": "CS303", "Time": "MW 9:30AM", "Location": "EMS",
                                     "Type": "L", "status": "create_LabSection"}, follow=True)
            self.assertEqual(301, LabSection.objects.get(section_number=301).section_number,
                             msg="Message for successful course section creation failed")

        def test_InvalidCreateCourseSection1(self):
            resp = self.client.post('course-management/',
                                    {"section_id": 222, "section_number": 301,
                                     "course_section": '',
                                     "course": "CS303", "Time": "MW 9:30AM", "Location": "EMS",
                                     "Type": "L", "status": "create_LabSection"}, follow=True)
            self.assertEqual(resp.context['message'], "Lab section missing a field or is a duplicate",
                             msg="Message for unsuccessful course section creation failed")

        def test_InvalidCreateCourseSection2(self):
            resp = self.client.post('course-management/',
                                    {"section_id": 222, "section_number": 302,
                                     "course_section": 303,
                                     "course": "CS303", "Time": "MW 9:30AM", "Location": "EMS",
                                     "Type": "L", "status": "create_LabSection"}, follow=True)
            self.assertEqual(resp.context['message'], "Course section missing a field or is a duplicate",
                             msg="Message for unsuccessful course section creation failed")

    class SupervisorDeleteLabSectionTest(TestCase):
        def setUp(self):
            self.temp3 = User(name="Test3", username="test_user3", password="PASSWORD3", email="test3@uwm.edu",
                              phone_number=1234567894, address="222 1st street", type="TA")
            self.temp_course = Course(course_id="CS303", course_name="Test Course", course_term="F")
            self.test_courseSection = CourseSection(section_id=123, section_number=303, course=self.temp_course,
                                                    Time="MW 9:30AM", Location="EMS", credits=3, instructor=self.temp2)
            self.test_lab_section = LabSection(section_id=222, section_number=302,
                                               course_section=self.test_courseSection,
                                               course=self.temp_course, Time="MW 9:30AM", Location="EMS",
                                               Type="L", ta=self.temp3)
            self.temp3.save()
            self.temp_course.save()
            self.test_courseSection.save()
            self.test_lab_section.save()
            self.client = Client()
            session = self.client.session
            session['username'] = 'test_user'
            session.save()

        def tearDown(self):
            self.temp3.delete()
            self.temp_course.delete()
            self.test_courseSection.delete()
            self.test_lab_section.delete()

        def test_ValidDeleteLabSection1(self):
            resp = self.client.post('course-management/',
                                    {"section_id": 222, "status": "delete_labSection"}, follow=True)
            self.assertEqual(resp.context['message'], "Lab Section Deletion successful",
                             msg="Message for successful course section creation failed")

        def test_ValidDeleteLabSection2(self):
            resp = self.client.post('course-management/',
                                    {"section_id": 222, "status": "delete_labSection"}, follow=True)
            self.assertEqual([], functions.LabSection_func.get(self, "section_id", "222"),
                             msg="Message for successful course section creation failed")

        def test_InvalidDeleteLabSection1(self):
            resp = self.client.post('course-management/',
                                    {"section_id": 45600, "status": "delete_labSection"}, follow=True)
            self.assertEqual(resp.context['message'], "Course section does not exist",
                             msg="Message for successful course section creation failed")


class SupervisorEditCourseTest(TestCase):
    def setUp(self):
        self.Course = Course(course_name="Chemistry 101")
        self.Course.save()
        self.client = Client()

    def validCourseEdit(self):
        response = self.client.post('/homepage/',
                                    {"course_name": "Chemistry 101", "editdata": {"course_name": "Chemistry 102"},
                                     "status": "edit_course"})

        with self.assertRaises(ObjectDoesNotExist):
            Course.objects.get(course_name="Chemistry 101")

    def invalidCourseEdit(self):
        response = self.client.post('/homepage/',
                                    {"course_name": "Chemistry 102", "editdata": {"course_name": "Chemistry 103"},
                                     "status": "edit_course"})

        self.assertEqual(response.content, "Course does not exist to be edited")


"""
PBI: As a supervisor I would like to assign users to courses so that the proper faculty and registered students are enrolled
"""


class SupervisorAssignUserToCourseTest(TestCase):
    def __init__(self):
        self.client = Client()
