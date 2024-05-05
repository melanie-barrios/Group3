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

    def post(self, request):

        if request.POST.get('deleteaccount') == "true":
            try:

                identity = request.POST['delusername']
                functions.User_func.Delete(self, identity)
                return render(request,'accountmanagement.html', {'message': 'Account Deleted Successfully'})
            except Exception as e:
                print(e)
                return render(request,'accountmanagement.html', {'message': 'Account Deletion Failed', 'error': str(e)})
        elif request.POST.get('createaccount') == "true":
            try:
                status = functions.User_func.Create(self, {"username": request.POST.get('createusername'), "password": request.POST.get('createpassword'), "email": request.POST.get('email'), "name": request.POST.get('name'), "phone_number": request.POST.get('phone'), "address":request.POST.get('address'), "type":request.POST.get('role')})
                if status is False:
                    raise Exception("Account not created")
                return render(request, 'accountmanagement.html', {'message': 'Account Created Successfully'})
            except Exception as e:
                print(e)
                return render(request, 'accountmanagement.html', {'message': 'Account Creation Failed', 'error': str(e)})

        else:
            return render(request, 'accountmanagement.html', {'message': 'No Account Function Selected'})



class CourseManagement(View):
    def get(self, request):
        return render(request, 'coursemanagement.html')

    def post(self, request):

        if request.POST.get('createcourse') == "true":
            try:

                status = functions.Course_func.Create(self, {"course_id": request.POST.get("courseid"), "course_name": request.POST.get('name'), "course_term": request.POST.get('term')})
                if status is False:
                    raise Exception("Course not created")
                return render(request, 'coursemanagement.html', {'message': 'Course Created Successfully'})
            except Exception as e:
                return render(request, 'coursemanagement.html',{'message': 'Course Creation Failed', 'error': str(e)})
        elif request.POST.get('createcoursesection') == "true":
            try:
                status = functions.CourseSection_func.Create(self, {"section_id": request.POST.get('sectionid'), "course": request.POST.get('course'), "section_number": request.POST.get('sectionnumber'), "Time": request.POST.get('time'), "Location": request.POST.get('location'), "credits": request.POST.get('credits'), "instructor": request.POST.get('instructor')})
                if status is False:
                    raise Exception("Course Section not created")
                return render(request, 'coursemanagement.html', {'message': 'Course Section Created Successfully'})
            except Exception as e:
                return render(request, 'coursemanagement.html', {'message': 'Course Section Creation Failed', 'error': str(e)})
        else:
            return render(request, 'coursemanagement.html', {'message': 'No Account Function Selected'})
