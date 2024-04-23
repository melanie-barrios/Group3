from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from .models import User, Instructor, TA, Course, LabSection, Supervisor
import TA_APP.functions as functions

class Login(View):
    def get(self, request):
        return render(request, 'login.html',{})

    def post(self, request):
        """Add a test user"""
        """test = User(user_id=5, name="Test", username="test_user5", password="PASSWORD5", email="test@uwm.edu",
                    phone_number=1234567890, address="123 1st street")
        test.save()"""
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
