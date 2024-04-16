from django.test import TestCase, Client
from .models import User,Instructor,TA,Course,LabSection
import functions

class UserTests(TestCase):

    def setUp(self):

        temp = User(user_id=1,name="Test",username="test_user",password="PASSWORD",email="test@uwm.edu",phone_number=1234567890,address="123 1st street")
        temp.save()
    def test_get_user_info(self):
        test_dic = {'user_id':1,'name':'Test','username':'test_user','password':'PASSWORD','email':'test@uwm.edu','phone_number':1234567890,'address':'123 1st Street' }
        self.assertEqual(test_dic,functions.User.get_user_info(1),msg="User not found")

    def test_get_user_info_2(self):
        self.assertEqual({},functions.User.get_user_info(2),msg="User not found")


