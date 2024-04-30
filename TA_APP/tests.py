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
                         phone_number=1234567890, address="123 1st street", type="TA")
        self.temp.save()
        self.temp3 = User(name="Test3", username="test_user3", password="PASSWORD3", email="test3@uwm.edu",
                          phone_number=1234567890, address="123 1st street", type="I")
        self.temp3.save()

    def tearDown(self):
        self.temp.delete()
        self.temp3.delete()

    def test_get_user_info_1(self):
        test_dic = {'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA"}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.User_func.get(self, query='username', identity='test_user'),
                         msg="User not found")

    def test_get_user_info_2(self):
        test_dic = {'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA"}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.User_func.get(self, query='name', identity='Test'), msg="User not found")

    def test_get_user_info_3(self):
        test_dic = {'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA"}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.User_func.get(self, query='password', identity='PASSWORD'),
                         msg="User not found")

    def test_get_user_info_4(self):
        test_dic = {'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA"}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.User_func.get(self, query='email', identity='test@uwm.edu'),
                         msg="User not found")

    def test_get_user_info_5(self):
        test_list = [{'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                      'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', 'type': "TA"},
                     {'name': 'Test3', 'username': 'test_user3', 'password': 'PASSWORD3',
                      'email': 'test3@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', 'type': "I"}]
        self.assertEqual(test_list, functions.User_func.get(self, query='phone_number', identity=1234567890),
                         msg="User not found")

    def test_get_user_info_6(self):
        test_list = [{'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                      'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', 'type': "TA"},
                     {'name': 'Test3', 'username': 'test_user3', 'password': 'PASSWORD3',
                      'email': 'test3@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', 'type': "I"}]
        self.assertEqual(test_list, functions.User_func.get(self, query='address', identity='123 1st Street'),
                         msg="User not found")

    def test_get_user_info_7(self):
        test_dic = {'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA"}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.User_func.get(self, query="type", identity="TA"), msg="User not found")

    def test_get_user_info_8(self):
        self.assertEqual({}, functions.User_func.get(self, query="username", identity="test_user2"),
                         msg="User not found")

    def test_get_all_users(self):
        test_list = [{'name': 'Test', 'username': 'test_user', 'password': 'PASSWORD',
                      'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', 'type': "TA"},
                     {'name': 'Test3', 'username': 'test_user3', 'password': 'PASSWORD3',
                      'email': 'test3@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', 'type': "I"}]
        self.assertEqual(test_list, functions.User_func.get_all(self),
                         msg="List of users not found in database when they should be")

    def test_create_user_1(self):
        test_dic = {'name': 'Test4', 'username': 'test_user4', 'password': 'PASSWORD4',
                    'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA"}
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

    def test_edit_user_info_1(self):
        test_dic = {'username': 'test_user', 'name': 'New-Test'}
        new_list = [{'name': 'New-Test', 'username': 'test_user', 'password': 'PASSWORD',
                     'email': 'test@uwm.edu', 'phone_number': 1234567890, 'address': '123 1st Street', "type": "TA"}]
        functions.User_func.Edit(self, info=test_dic)
        self.assertEqual(new_list, functions.User_func.get(self, query="username", identity="test_user"),
                         msg="User information not updated")

    def test_edit_user_info_2(self):
        test_dic = {'username': 'test_user', 'name': 'New-Test'}
        self.assertEqual(True, functions.User_func.Edit(self, info=test_dic),
                         msg="Should return true becuase user exist")

    def test_edit_user_info_3(self):
        test_dic = {}
        self.assertEqual(False, functions.User_func.Edit(self, info=test_dic),
                         msg="Should return false because input dictionary does not exist")

    def test_edit_user_info_4(self):
        test_dic = {'username': 'test_user17', 'name': 'New-Test'}
        self.assertEqual(False, functions.User_func.Edit(self, info=test_dic),
                         msg="Should return false because user does not exist")

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
                         msg="User not found")
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
        test_dic = {'course_id': 'CS101', "course_term": "Spring"}
        self.assertEqual(True, functions.Course_func.Edit(self, test_dic),
                         msg="Should return true because course exists")

    def test_update_course_info_3(self):
        test_dic = {'course_id': 'CS1010', "course_term": "Spring"}
        self.assertEqual(False, functions.Course_func.Edit(self, test_dic),
                         msg="Should return false because course does not exists")

    def test_update_course_info_4(self):
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



class LabSectionTests(TestCase):
    def setUp(self):
        self.test_course = Course(course_id="22222", course_name="Test Lab Course", course_term="F")
        self.test_course.save()
        self.test_course_section = CourseSection(section_id=456, section_number=201, course=self.test_course)
        self.test_course_section.save()
        self.test_lab_section = LabSection(section_id=789, section_number=301, course_section=self.test_course_section,
                                           course=self.test_course)
        self.test_lab_section.save()

    def tearDown(self):
        self.test_lab_section.delete()
        self.test_course_section.delete()
        self.test_course.delete()

    def test_get_labSection_info(self):
        test_dic = {'section_id': '789', 'section_number': '301'}
        test_list = [test_dic]
        self.assertEqual(test_list, functions.LabSection_func.get(query='section_id', identity='789'))

    def test_get_labSection_info_fail(self):
        self.assertEqual(False, functions.LabSection_func.get(query='section_id', identity='999'))

    def test_create_labSection(self):
        info = {"section_id": 987, "section_number": 302, "course_section": self.test_course_section,
                "course": self.test_course}
        self.assertTrue(functions.LabSection_func.Create(info))

    def test_create_labSection_fail(self):
        info = {"section_number": 302, "course_section": self.test_course_section,
                "course": self.test_course}
        self.assertEqual(False, functions.LabSection_func.Create(info),
                         msg="Cannot create lab section without section id")

    def test_create_labSection_fail2(self):
        info = {"section_id": 987, "section_number": 302, "course_section": self.test_course_section}
        self.assertEqual(False, functions.LabSection_func.Create(info),
                         msg="Cannot create lab section without assigning course")

    def test_edit_labSection(self):
        update_info = {"section_id": 789, "section_number": 401, "course_section": self.test_course_section,
                       "course": self.test_course}
        functions.LabSection_func.Edit(update_info)
        self.assertEquals(update_info, functions.LabSection_func.get(query='section_id', identity='789'))

    def test_delete_labSection(self):
        identity = "789"
        self.assertTrue(functions.LabSection_func.Delete(identity))


class TATests(TestCase):
    def setup(self):
        temp_user = User(user_id=1, name="Test", username="test_user", password="PASSWORD", email="test@uwm.edu",
                         phone_number=1234567890, address="123 1st street")
        temp_user.save()
        ta_1 = TA(user_id=temp_user, ta_id=1)
        ta_1.save()


    def test_get_ta_info_1(self):
        test_dic = {"user_id": 1, "ta_id": 1}
        self.assertEqual(test_dic, functions.TA_func.get_ta_info(self, 1),
                         msg="Should be equal since TA is in the database")

    def test_get_ta_info_2(self):
        test_dic = {}
        self.assertEqual(test_dic, functions.TA_func.get_ta_info(self, 2),
                         msg="Should be equal since TA is not in the database")

    def test_update_ta_info_1(self):
        new_dic = {"user_id": 2, "ta_id": 1}
        functions.TA_func.update_ta_info(self, new_dic)
        self.assertEqual(new_dic, functions.TA_func.get_ta_info(self, 2),
                         msg="Should be equal because of updating user")

    def test_update_ta_info_2(self):
        new_dic = {"user_id": 2, "ta_id": 1}
        self.assertEqual(True, functions.TA_func.update_ta_info(self, new_dic),
                         msg="Should be equal because user exists in database")

    def test_update_ta_info_3(self):
        new_dic = {"user_id": 2, "ta_id": 2}
        self.assertEqual(False, functions.TA_func.update_ta_info(self, new_dic),
                         msg="Should be equal because user does not exists in database")

    def test_update_ta_info_4(self):
        new_dic = {}
        self.assertEqual(False, functions.TA_func.update_ta_info(self, new_dic),
                         msg="Should be equal because dictionary is empty")

    def test_delete_ta_1(self):
        functions.TA_func.delete_ta(self, ta_id=1)
        self.assertEqual({}, functions.TA_func.get_ta_info(self, ta_id=1),
                         msg="Should be equal since TA exists in database and should be deleted")

    def test_delete_ta_2(self):
        self.assertEqual(False, functions.TA_func.delete_ta(self, ta_id=2),
                         msg="Should return false since TA does not exist")


class InstructorTests(TestCase):

    def setUp(self):
        user = User(user_id=1, name="Test", username="test_user", password="PASSWORD", email="test@uwm.edu",
                    phone_number=1234567890, address="123 1st street")
        user.save()
        user2 = User(user_id=3, name="Test3", username="test_user3", password="PASSWORD3", email="test3@uwm.edu",
                     phone_number=1234567890, address="123 1st street")
        user2.save()
        instructor = Instructor(user_id=user, instructor_id=1)
        instructor.save()
        instructor2 = Instructor(user_id=user2, instructor_id=2)
        instructor2.save()

    def test_get_instructor_info_1(self):
        test_dic = {"user_id": 1, "instructor_id": 1}
        self.assertEqual(test_dic, functions.Instructor_func.get_instructor_info(self, 1),
                         msg="Should be equal since instructor is in the database")

    def test_get_instructor_info_2(self):
        test_dic = {}
        self.assertEqual(test_dic, functions.Instructor_func.get_instructor_info(self, 3),
                         msg="Should be equal since instructor is not in the database")

    def test_get_all_instructors(self):
        test_list = [{"user_id": 1, "instructor_id": 1}, {"user_id": 1, "instructor_id": 2}]
        self.assertEqual(test_list, functions.Instructor_func.get_all_instructors(self),
                         msg="Should be equal since instructors are in the database")
