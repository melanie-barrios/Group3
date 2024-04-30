from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from .models import User, Course, LabSection, CourseSection
import TA_APP.functions as functions

class Login(View):
    def get(self, request):
        """Add test supervisor"""
        """test = User(name="Test", username="test_user5", password="PASSWORD5", email="test@uwm.edu",
                    phone_number=1234567890, address="123 1st street",type="S")
        test.save()"""
        return render(request, 'login.html',{})

    def post(self, request):

        """Grab form fields"""
        username = request.POST['username']
        password = request.POST['password']
        """check identity"""
        verify = functions.Login.authenticate(self,str(username),str(password))

        """If user is valid move to home page"""
        if verify:
            request.session['username'] = username
            return redirect('/homepage/')
        else:
            return render(request, "login.html", {"message": "Username or password is incorrect"})

class HomePage(View):

    def get(self, request):
        print(request.session['username'])
        if not request.session['username'] == "":
            return render(request, 'homepage.html',{})
        else:
            return redirect('/')

    def post(self,request):
        """logout(request)"""

        """try:
            del request.session["username"]
        except KeyError:
            pass"""
        """request.session.clear()"""
        request.session["username"] = ""
        return redirect('/')

class AccountManagement(View):
    def get(self, request):
        return render(request, 'accountmanagement.html')

class CourseManagement(View):
    def get(self, request):
        return render(request, 'coursemanagement.html')
