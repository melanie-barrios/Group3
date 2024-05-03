from django.test import TestCase, Client
from .models import User, Course, LabSection, CourseSection
import TA_APP.functions as functions


class LoginTest(TestCase):

    def setUp(self):
        self.temp = User(name="Test", username="test_user", password="PASSWORD", email="test@uwm.edu",
                         phone_number=1234567890, address="123 1st street", type="I")
        self.temp.save()

    def tearDown(self):
        self.temp.delete()

    def test_login_1(self):
        self.assertEqual(True, functions.Login.authenticate(self, username="test_user", password="PASSWORD"),
                         msg="User exists should return true")

    def test_login_2(self):
        self.assertEqual(False, functions.Login.authenticate(self, username="test_user", password="WORD"),
                         msg="Wrong password should return false")

    def test_login_3(self):
        self.assertEqual(False, functions.Login.authenticate(self, username="test_user2", password="WORD"),
                         msg="Wrong user should return false")


class UserTests(TestCase):

    def setUp(self):
        self.temp = User(name="Test", username="test_user", password="PASSWORD", email="test@uwm.edu",
                         phone_number=1234567890, address="123 1st Street", type="TA")
        self.temp.save()
        self.temp3 = User(name="Test3", username="test_user3", password="PASSWORD3", email="test3@uwm.edu",
                          phone_number=1234567890, address="123 1st Street", type="I")
        self.temp3.save()

    def tearDown(self):
        self.temp.delete()
        self.temp3.delete()

    def test_get_user_info_1(self):
        test_dic = {'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA", "skills": ''}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.User_func.get(self, query='username', identity='test_user'),
                         msg="User not found")

    def test_get_user_info_2(self):
        test_dic = {'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA", "skills": ''}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.User_func.get(self, query='name', identity='Test'), msg="User not found")

    def test_get_user_info_3(self):
        test_dic = {'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA", "skills": ''}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.User_func.get(self, query='password', identity='PASSWORD'),
                         msg="User not found")

    def test_get_user_info_4(self):
        test_dic = {'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA", "skills": ''}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.User_func.get(self, query='email', identity='test@uwm.edu'),
                         msg="User not found")

    def test_get_user_info_5(self):
        test_list = [{'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                      'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', 'type': "TA", 'skills': ''},
                     {'name': 'Test3', 'username': 'test_user3', 'password': 'PASSWORD3',
                      'email': 'test3@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', 'type': "I", 'skills': ''}]
        self.assertEqual(test_list, functions.User_func.get(self, query='phone_number', identity=str(1234567890)),
                         msg="User not found")

    def test_get_user_info_6(self):
        test_list = [{'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                      'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', 'type': "TA", 'skills': ''},
                     {'name': 'Test3', 'username': 'test_user3', 'password': 'PASSWORD3',
                      'email': 'test3@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', 'type': "I", 'skills': ''}]
        self.assertEqual(test_list, functions.User_func.get(self, query='address', identity='123 1st Street'),
                         msg="User not found")

    def test_get_user_info_7(self):
        test_dic = {'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA", 'skills': ''}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.User_func.get(self, query="type", identity="TA"), msg="User not found")

    def test_get_user_info_8(self):
        self.assertEqual([], functions.User_func.get(self, query="username", identity="test_user2"),
                         msg="User not found")

    def test_get_all_users(self):
        test_list = [{'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                      'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', 'type': "TA", 'skills': ''},
                     {'name': 'Test3', 'username': 'test_user3', 'password': 'PASSWORD3',
                      'email': 'test3@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', 'type': "I", 'skills': ''}]
        self.assertEqual(test_list, functions.User_func.get_all(self),
                         msg="List of users not found in database when they should be")

    def test_create_user_1(self):
        test_dic = {'name': 'Test4', 'username': 'test_user4', 'password': 'PASSWORD4',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA", 'skills': ''}
        test_list = [test_dic]
        functions.User_func.Create(self, info=test_dic)
        self.assertEqual(test_list, functions.User_func.get(self, query='username', identity='test_user4'),
                         msg="User not found")
        temp_user = User.objects.get(username="test_user4")
        temp_user.delete()

    def test_create_user_2(self):
        test_dic = {'name': 'Test4', 'username': 'test_user4', 'password': 'PASSWORD4',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA"}
        self.assertEqual(True, functions.User_func.Create(self, info=test_dic),
                         msg="Operation should have been successful")
        temp_user = User.objects.get(username="test_user4")
        temp_user.delete()

    def test_create_user_3(self):
        test_dic = {'name': 'Test4', 'username': 'test_user4', 'password': 'PASSWORD4',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA",
                    'skills': 'HTML'}
        self.assertEqual(True, functions.User_func.Create(self, info=test_dic),
                         msg="Operation should have been successful")
        temp_user = User.objects.get(username="test_user4")
        temp_user.delete()

    def test_create_user_4(self):
        test_dic = {'name': 'Test4', 'username': 'test_user4'}
        self.assertEqual(False, functions.User_func.Create(self, info=test_dic),
                         msg="Incorrect dictionary operation is should be unsuccessful")

    def test_create_user_5(self):
        test_dic = {}
        self.assertEqual(False, functions.User_func.Create(self, info=test_dic),
                         msg="Empty dictionary operation is unsuccessful")

    def test_create_user_6(self):
        test_dic = {'name': 'Test4', 'username': 'test_user', 'password': 'PASSWORD4',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA",
                    'skills': 'HTML'}
        self.assertEqual(False, functions.User_func.Create(self, info=test_dic),
                         msg="Operation should have been successful cannot have repeated usernames")

    def test_edit_user_info_1(self):
        test_dic = {'username': 'test_user', 'name': 'New-Test'}
        new_list = [{'name': 'New-Test', 'username': 'test_user', 'password': 'PASSWORD',
                     'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA", 'skills': ''}]
        functions.User_func.Edit(self, info=test_dic)
        self.assertEqual(new_list, functions.User_func.get(self, query="username", identity="test_user"),
                         msg="User information not updated")

    def test_edit_user_info_2(self):
        test_dic = {'username': 'test_user', 'name': 'New-Test', 'address': '321 1st Street'}
        new_list = [{'name': 'New-Test', 'username': 'test_user', 'password': 'PASSWORD',
                     'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '321 1st Street', "type": "TA", 'skills': ''}]
        functions.User_func.Edit(self, info=test_dic)
        self.assertEqual(new_list, functions.User_func.get(self, query="username", identity="test_user"),
                         msg="User information not updated")

    def test_edit_user_info_3(self):
        test_dic = {'username': 'test_user', 'name': 'New-Test'}
        self.assertEqual(True, functions.User_func.Edit(self, info=test_dic),
                         msg="Should return true because user exist")

    def test_edit_user_info_4(self):
        test_dic = {}
        self.assertEqual(False, functions.User_func.Edit(self, info=test_dic),
                         msg="Should return false because input dictionary does not exist")

    def test_edit_user_info_5(self):
        test_dic = {'username': 'test_user17', 'name': 'New-Test'}
        self.assertEqual(False, functions.User_func.Edit(self, info=test_dic),
                         msg="Should return false because user does not exist")

    def test_edit_user_info_6(self):
        test_dic = {'name': 'New-Test'}
        self.assertEqual(False, functions.User_func.Edit(self, info=test_dic),
                         msg="Should return false because username is required")

    def test_delete_user_1(self):
        self.assertEqual(True, functions.User_func.Delete(self, identity='test_user'),
                         "User should successfully delete")

    def test_delete_user_2(self):
        self.assertEqual(False, functions.User_func.Delete(self, identity='test_user81'),
                         "User should not exist in the database")

    def test_delete_user_3(self):
        functions.User_func.Delete(self, identity='test_user')
        self.assertEqual([], functions.User_func.get(self, query="username", identity='test_user'),
                         "User should not exist in the database")


class CourseTests(TestCase):

    def setUp(self):
        self.temp = User(name="Test", username="test_user", password="PASSWORD", email="test@uwm.edu",
                         phone_number=1234567890, address="123 1st street", type="TA")
        self.temp.save()
        self.temp3 = User(name="Test3", username="test_user3", password="PASSWORD3", email="test3@uwm.edu",
                          phone_number=1234567890, address="123 1st street", type="I")
        self.temp3.save()
        self.temp_course = Course(course_id="CS101", course_name="Test Course", course_term="F")
        self.temp_course.save()
        self.temp2_course = Course(course_id="CS102", course_name="Test Course 2", course_term="F")
        self.temp2_course.save()
        self.section = CourseSection(section_id="11111", section_number=801,
                                     course=self.temp_course, Time="MW 9:30AM", Location="EMS", credits=3,
                                     instructor=self.temp3)
        self.section.save()
        self.section2 = CourseSection(section_id="11112", section_number=801,
                                      course=self.temp2_course, Time="MW 9:30AM", Location="EMS", credits=3,
                                      instructor=self.temp3)
        self.section2.save()

    def tearDown(self):
        self.temp.delete()
        self.temp3.delete()
        self.temp_course.delete()
        self.temp2_course.delete()
        self.section.delete()
        self.section2.delete()

    def test_get_course_info_1(self):
        test_dic = {'course_id': 'CS101', "course_name": "Test Course", "course_term": "Fall",
                    "Course Section 1": {"section_id": "11111", "section_number": 801, "Time": "MW 9:30AM",
                                         "Location": "EMS", "credits": 3, "instructor": "Test3"}}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.Course_func.get(self, query="course_id", identity="CS101"),
                         msg="Course exists in the database should match result")

    def test_get_course_info_2(self):
        test_dic = {'course_id': 'CS101', "course_name": "Test Course", "course_term": "Fall",
                    "Course Section 1": {"section_id": "11111", "section_number": 801, "Time": "MW 9:30AM",
                                         "Location": "EMS", "credits": 3, "instructor": "Test3"}}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.Course_func.get(self, query="course_name", identity="Test Course"),
                         msg="Course exists in the database should match result")

    def test_get_course_info_3(self):
        test_dic = {'course_id': 'CS101', "course_name": "Test Course", "course_term": "Fall",
                    "Course Section 1": {"section_id": "11111", "section_number": 801, "Time": "MW 9:30AM",
                                         "Location": "EMS", "credits": 3, "instructor": "Test3"}}
        test_dic2 = {'course_id': 'CS102', "course_name": "Test Course 2", "course_term": "Fall",
                     "Course Section 1": {"section_id": "11112", "section_number": 801, "Time": "MW 9:30AM",
                                          "Location": "EMS", "credits": 3, "instructor": "Test3"}}
        test_list = [test_dic, test_dic2]
        self.assertEqual(test_list, functions.Course_func.get(self, query="course_term", identity="Fall"),
                         msg="Course exists in the database should match result")

    def test_get_course_info_4(self):
        test_list = []
        self.assertEqual(test_list, functions.Course_func.get(self, query="course_id", identity="CS1000"),
                         msg="Course does not exist result should be empty")

    def test_get_all_courses(self):
        test_dic = {'course_id': 'CS101', "course_name": "Test Course", "course_term": "Fall",
                    "Course Section 1": {"section_id": "11111", "section_number": 801, "Time": "MW 9:30AM",
                                         "Location": "EMS", "credits": 3, "instructor": "Test3"}}
        test_dic2 = {'course_id': 'CS102', "course_name": "Test Course 2", "course_term": "Fall",
                     "Course Section 1": {"section_id": "11112", "section_number": 801, "Time": "MW 9:30AM",
                                          "Location": "EMS", "credits": 3, "instructor": "Test3"}}
        test_list = [test_dic, test_dic2]
        self.assertEqual(test_list, functions.Course_func.get_all(self), msg="Courses not showing up properly")

    def test_create_course_1(self):
        test_dic = {'course_id': 'CS201', "course_name": "Test Course 201", "course_term": "Fall"}
        test_list = [test_dic]
        functions.Course_func.Create(self, info=test_dic)
        self.assertEqual(test_list, functions.User_func.get(self, query='course_id', identity='CS201'),
                         msg="Course not found")
        temp_user = Course.objects.get(course_id="CS201")
        temp_user.delete()

    def test_create_course_2(self):
        test_dic = {'course_id': 'CS201', "course_name": "Test Course 201", "course_term": "Fall"}
        self.assertEqual(True, functions.Course_func.Create(self, info=test_dic),
                         msg="Operation should have been successful")
        temp_user = Course.objects.get(course_id="CS201")
        temp_user.delete()

    def test_create_course_3(self):
        test_dic = {'course_id': 'CS201', "course_term": "Fall"}
        self.assertEqual(False, functions.Course_func.Create(self, info=test_dic),
                         msg="Incorrect dictionary operation is should be unsuccessful")

    def test_create_course_4(self):
        test_dic = {}
        self.assertEqual(False, functions.Course_func.Create(self, info=test_dic),
                         msg="Empty dictionary operation is unsuccessful")

    def test_create_course_5(self):
        test_dic = {'course_id': 'CS101', "course_name": "Test Course 201", "course_term": "Fall"}
        self.assertEqual(False, functions.Course_func.Create(self, info=test_dic),
                         msg="Operation should not have been successful because you cannot repeat course ID")

    def test_edit_course_info_1(self):
        test_dic = {'course_id': 'CS101', "course_term": "Spring"}
        updated_dic = {'course_id': 'CS101', "course_name": "Test Course", "course_term": "Spring",
                       "Course Section 1": {"section_id": "11111", "section_number": 801, "Time": "MW 9:30AM",
                                            "Location": "EMS", "credits": 3, "instructor": "Test3"}}
        updated_list = [updated_dic]
        functions.Course_func.Edit(self, info=test_dic)
        self.assertEqual(updated_list, functions.Course_func.get(self, query="course_id", identity="CS101"),
                         msg="Course should be updated with new term")

    def test_edit_course_info_2(self):
        test_dic = {'course_id': 'CS101', "course_name": "Test course 200", "course_term": "Spring"}
        updated_dic = {'course_id': 'CS101', "course_name": "Test course 200", "course_term": "Spring",
                       "Course Section 1": {"section_id": "11111", "section_number": 801, "Time": "MW 9:30AM",
                                            "Location": "EMS", "credits": 3, "instructor": "Test3"}}
        updated_list = [updated_dic]
        functions.Course_func.Edit(self, info=test_dic)
        self.assertEqual(updated_list, functions.Course_func.get(self, query="course_id", identity="CS101"),
                         msg="Course should be updated with new term")

    def test_edit_course_info_3(self):
        test_dic = {'course_id': 'CS101', "course_term": "Spring"}
        self.assertEqual(True, functions.Course_func.Edit(self, test_dic),
                         msg="Should return true because course exists")

    def test_edit_course_info_4(self):
        test_dic = {'course_id': 'CS1010', "course_term": "Spring"}
        self.assertEqual(False, functions.Course_func.Edit(self, test_dic),
                         msg="Should return false because course does not exists")

    def test_edit_course_info_5(self):
        test_dic = {'course_id': 'CS1010', "course_term": "Spring"}
        self.assertEqual(False, functions.Course_func.Edit(self, test_dic),
                         msg="Should return false because course does not exists")

    def test_edit_course_info_6(self):
        test_dic = {}
        self.assertEqual(False, functions.Course_func.Edit(self, test_dic),
                         msg="Should return false because dictionary is empty")

    def test_delete_course_1(self):
        self.assertEqual(True, functions.Course_func.Delete(self, identity='CS101'),
                         "User should successfully delete")

    def test_delete_course_2(self):
        self.assertEqual(False, functions.Course_func.Delete(self, identity='CS2000'),
                         "User should not exist in the database")

    def test_delete_course_3(self):
        functions.Course_func.Delete(self, identity='CS101')
        self.assertEqual([], functions.Course_func.get(self, query="course_id", identity='CS101'),
                         "User should not exist in the database")


class CourseSectionTests(TestCase):
    def setUp(self):
        self.temp = User(name="Test", username="test_user", password="PASSWORD", email="test@uwm.edu",
                         phone_number=1234567890, address="123 1st street", type="Instructor")
        self.temp_course = Course(course_id="CS202", course_name="Test Course", course_term="F")
        self.test_courseSection = CourseSection(section_id=456, section_number=201, course=self.temp_course,
                                                Time="MW 9:30AM", Location="EMS", credits=3, instructor=self.temp)
        self.test_courseSection1 = CourseSection(section_id=567, section_number=501, course=self.temp_course,
                                                 Time="TTH 9:30AM", Location="EMS", credits=3, instructor=self.temp)
        self.temp.save()
        self.temp_course.save()
        self.test_courseSection.save()
        self.test_courseSection1.save()

    def tearDown(self):
        self.temp.delete()
        self.temp_course.delete()
        self.test_courseSection.delete()
        self.test_courseSection1.delete()

    def test_get_Course_Section_info(self):
        test_dic = {"section_id": 456, "section_number": 201, "course": self.temp_course.course_id, "Time": "MW 9:30AM",
                    "Location": "EMS", "credits": 3, "instructor": self.temp.name}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.CourseSection_func.get(self, query='section_id', identity='456'))

    def test_get_Course_Section_info_fail(self):
        self.assertEqual([], functions.CourseSection_func.get(self, query='section_id', identity='999'))

    def test_getAll_Course_Section_info(self):
        test_dic = {"section_id": 456, "section_number": 201, "course": self.temp_course.course_id,
                    "Time": "MW 9:30AM", "Location": "EMS", "credits": 3, "instructor": self.temp.name}
        test_dic1 = {"section_id": 567, "section_number": 501, "course": self.temp_course.course_id,
                     "Time": "TTH 9:30AM", "Location": "EMS", "credits": 3, "instructor": self.temp.name}
        expected_list = [test_dic, test_dic1]
        self.assertEqual(expected_list, functions.CourseSection_func.get_all(self))

    def test_create_Course_Section(self):
        info = {"section_id": 345, "section_number": 300, "course": self.temp_course, "Time": "MW 5:30PM",
                "Location": "EMS", "credits": 3, "instructor": self.temp}
        self.assertTrue(self, functions.CourseSection_func.Create(self, info))

    def test_create_Course_Section_fail(self):
        info = {"section_number": 201, "course": self.temp_course, "Time": "MW 9:30AM",
                "Location": "EMS", "credits": 3, "instructor": "Test3"}
        self.assertEqual(False, functions.CourseSection_func.Create(self, info),
                         msg="Cannot create course section without section id")

    def test_create_Course_Section_fail2(self):
        info = {"section_id": "22222", "section_number": 801, "Time": "MW 9:30AM",
                "Location": "EMS", "credits": 3, "instructor": "Test3"}
        self.assertEqual(False, functions.CourseSection_func.Create(self, info),
                         msg="Cannot create course section without assigning course")

    def test_create_Course_Section_fail3(self):
        info = {"section_id": 456, "section_number": 201, "course": self.temp_course, "Time": "MW 9:30AM",
                "Location": "EMS", "credits": 3, "instructor": self.temp}
        self.assertEqual(False, functions.CourseSection_func.Create(self, info),
                         msg="Cannot create course section that is already there")

    def test_create_Course_Section_fail4(self):
        info = {}
        self.assertEqual(False, functions.CourseSection_func.Create(self, info),
                         msg="Cannot create course section with an empty dictionary")

    def test_edit_Course_Section(self):
        update_info = {"section_id": 456, "Location": "Lubar Hall"}
        updated_info = {"section_id": 456, "section_number": 201, "course": self.temp_course.course_id,
                        "Time": "MW 9:30AM", "Location": "Lubar Hall", "credits": 3, "instructor": self.temp.name}
        updated_info_list = [updated_info]
        print("expected", updated_info_list)
        self.assertTrue(functions.CourseSection_func.Edit(self, update_info))
        print("result  ", functions.CourseSection_func.get(self, query='section_id', identity='456'))
        self.assertEqual(updated_info_list, functions.CourseSection_func.get(self, query='section_id', identity='456'))

    def test_edit_course_section_invalid_section_id(self):
        update_info = {"section_id": 999, "Location": "Lubar Hall"}
        self.assertFalse(functions.CourseSection_func.Edit(self, update_info))

    def test_delete_Course_Section(self):
        identity = "456"
        self.assertTrue(functions.CourseSection_func.Delete(self, identity))

    def test_delete_Course_Section_fail(self):
        identity = "000"
        self.assertFalse(functions.CourseSection_func.Delete(self, identity))

    def test_delete_Course_Section2(self):
        functions.CourseSection_func.Delete(self, "456")
        self.assertEqual([], functions.CourseSection_func.get(self, query="section_id", identity='456'))


class LabSectionTests(TestCase):
    def setUp(self):
        self.temp2 = User(name="Test2", username="test_user2", password="PASSWORD2", email="test2@uwm.edu",
                          phone_number=1234567893, address="123 1st street", type="Instructor")
        self.temp3 = User(name="Test3", username="test_user3", password="PASSWORD3", email="test3@uwm.edu",
                          phone_number=1234567894, address="222 1st street", type="TA")
        self.temp_course = Course(course_id="CS303", course_name="Test Course", course_term="F")
        self.test_courseSection = CourseSection(section_id=123, section_number=303, course=self.temp_course,
                                                Time="MW 9:30AM", Location="EMS", credits=3, instructor=self.temp2)
        self.test_lab_section = LabSection(section_id=222, section_number=301, course_section=self.test_courseSection,
                                           course=self.temp_course, Time="MW 9:30AM", Location="EMS",
                                           Type="L", ta=self.temp3)
        self.test_lab_section1 = LabSection(section_id=11111, section_number=801, course_section=self.test_courseSection,
                                            course=self.temp_course, Time="MW 9:30AM", Location="EMS", Type="L",
                                            ta=self.temp3)
        self.test_lab_section2 = LabSection(section_id=11112, section_number=802, course_section=self.test_courseSection,
                                            course=self.temp_course, Time="MW 9:30AM", Location="EMS", Type="L",
                                            ta=self.temp3)
        self.temp2.save()
        self.temp3.save()
        self.temp_course.save()
        self.test_courseSection.save()
        self.test_lab_section.save()
        self.test_lab_section1.save()
        self.test_lab_section2.save()

    def tearDown(self):
        self.temp2.delete()
        self.temp3.delete()
        self.temp_course.delete()
        self.test_courseSection.delete()
        self.test_lab_section.delete()
        self.test_lab_section1.delete()
        self.test_lab_section2.delete()

    def test_get_labSection_info(self):
        test_dic = {"section_id": 222, "section_number": 301, "course_section": self.test_courseSection.section_number,
                    "course": self.temp_course.course_id, "Time": "MW 9:30AM", "Location": "EMS",
                    "Type": "L", "ta": self.temp3.name}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.LabSection_func.get(self, query='section_id', identity='222'))

    def test_get_labSection_info_fail(self):
        self.assertEqual([], functions.LabSection_func.get(self, query='section_id', identity='999'))

    def test_getAll_labSection_info(self):
        test_dic = {"section_id": 222, "section_number": 301, "course_section": self.test_courseSection.section_number,
                    "course": self.temp_course.course_id, "Time": "MW 9:30AM", "Location": "EMS",
                    "Type": "L", "ta": self.temp3.name}
        test_dic1 = {'section_id': 11111, 'section_number': 801,
                     'course_section': self.test_courseSection.section_number,
                     'course': self.temp_course.course_id, 'Time': 'MW 9:30AM', 'Location': 'EMS',
                     'Type': 'L', 'ta': self.temp3.name}
        test_dic2 = {'section_id': 11112, 'section_number': 802,
                     'course_section': self.test_courseSection.section_number,
                     'course': self.temp_course.course_id, 'Time': 'MW 9:30AM', 'Location': 'EMS',
                     'Type': 'L', 'ta': self.temp3.name}
        expected_result = [test_dic, test_dic1, test_dic2]
        self.assertEqual(expected_result, functions.LabSection_func.get_all(self))

    def test_create_labSection(self):
        info = {"section_id": 987, "section_number": 302, "course_section": self.test_courseSection,
                "course": self.temp_course, "Time": "MW 9:30AM", "Location": "EMS", "Type": "L", "ta": self.temp3}
        self.assertTrue(functions.LabSection_func.Create(self, info))

    def test_create_labSection_fail(self):
        info = {"section_number": 302, "course_section": self.test_courseSection,
                "course": self.temp_course, "Time": "MW 9:30AM", "Location": "EMS", "Type": "L", "ta": self.temp3}
        self.assertEqual(False, functions.LabSection_func.Create(self, info),
                         msg="Cannot create lab section without section id")

    def test_create_labSection_fail2(self):
        info = {"section_id": 987, "section_number": 302, "course_section": self.test_courseSection,
                "Time": "MW 9:30AM", "Location": "EMS", "Type": "L", "ta": self.temp3}
        self.assertEqual(False, functions.LabSection_func.Create(self, info),
                         msg="Cannot create lab section without assigning course")

    def test_create_labSection_fail3(self):
        info = {"section_id": 222, "section_number": 301, "course_section": self.test_courseSection,
                "course": self.temp_course, "Time": "MW 9:30AM", "Location": "EMS", "Type": "L", "ta": self.temp3}
        self.assertEqual(False, functions.LabSection_func.Create(self, info),
                         msg="Cannot create lab section that is already there")

    def test_create_labSection_fail4(self):
        info = {}
        self.assertEqual(False, functions.LabSection_func.Create(self, info),
                         msg="Cannot create lab section with an empty dictionary")

    def test_edit_labSection(self):
        update_info = {"section_id": 222, "section_number": 401}
        updated_info = {"section_id": 222, "section_number": 401,
                        "course_section": self.test_courseSection.section_number,
                        "course": self.temp_course.course_id, "Time": "MW 9:30AM", "Location": "EMS",
                        "Type": "L", "ta": self.temp3.name}
        updated_info_list = [updated_info]
        self.assertTrue(functions.LabSection_func.Edit(self, update_info))
        self.assertEqual(updated_info_list, functions.LabSection_func.get(self, query='section_id', identity='222'))

    def test_edit_labSection_invalid_section_id(self):
        update_info = {"section_id": 999, "section_number": 401}
        self.assertFalse(functions.LabSection_func.Edit(self, update_info))

    def test_edit_labSection_invalid_ta(self):
        update_info = {"section_id": 222, "ta": "invalid_username"}
        self.assertFalse(functions.LabSection_func.Edit(self, update_info))

    def test_delete_labSection_invalid_section_id(self):
        identity = "999"
        self.assertFalse(functions.LabSection_func.Delete(self, identity))

    def test_delete_labSection(self):
        identity = "222"
        self.assertTrue(functions.LabSection_func.Delete(self, identity))
