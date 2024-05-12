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
        return render(request, 'login.html', {})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        """check identity"""
        verify = functions.Login.authenticate(self,str(username),str(password))

        """If user is valid move to home page"""
        if verify == 'S':  # Supervisor (or Administrator)
            request.session['username'] = username
            return render(request, 'homepage.html', {})
        elif verify == 'I':  # Instructor
            request.session['username'] = username
            return redirect('instructor_dashboard')
        elif verify == 'TA':  # TA
            request.session['username'] = username
            return redirect('ta_dashboard')
        else:
            return render(request, "login.html", {"message": "Username or password is incorrect"})


class HomePage(View):
    def get(self, request):
        if not request.session.get('username'):
            return redirect('/')

    def post(self, request):
        logout(request)
        return redirect('/')


class AccountManagement(View):
    def get(self, request):
        if request.session.get('username') and User.objects.get(username=request.session.get('username')).type == 'S':
            return render(request, 'accountmanagement.html')
        else:
            logout(request)
            return redirect('/')

    def post(self, request):

        if request.POST.get('status') == "delete":
            try:

                identity = request.POST['username']
                functions.User_func.Delete(self, identity)
                return render(request, 'accountmanagement.html', {'message': 'Account Deleted Successfully'})
            except Exception as e:

                return render(request, 'accountmanagement.html',
                              {'message': 'Account Deletion Failed', 'error': str(e)})
        elif request.POST.get('status') == "create":
            try:

                status = functions.User_func.Create(self, {"username": request.POST.get('username'),
                                                           "password": request.POST.get('password'),
                                                           "email": request.POST.get('email'),
                                                           "name": request.POST.get('name'),
                                                           "phone_number": request.POST.get('phone_number'),
                                                           "address": request.POST.get('address'),
                                                           "type": request.POST.get('type'),
                                                           "skills": request.POST.get('skills')})
                if status is False:
                    raise Exception("Account not created")
                return render(request, 'accountmanagement.html', {'message': 'Account Created Successfully'})
            except Exception as e:

                return render(request, 'accountmanagement.html',
                              {'message': "Duplicate username or missing form field"})
        elif request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')
        else:
            return render(request, 'accountmanagement.html', {'message': 'No Account Function Selected'})


class CourseManagement(View):
    def get(self, request):
        if request.session.get('username') and User.objects.get(username=request.session.get('username')).type == 'S':
            return render(request, 'coursemanagement.html', {"courses": functions.Course_func.get_all(self), "course_sections": functions.CourseSection_func.get_all(self), "lab_sections": functions.LabSection_func.get_all(self)})
        else:
            logout(request)
            return redirect('/')

    def post(self, request):
        if request.POST.get('createcourse') == "true":
            try:

                status = functions.Course_func.Create(self, {"course_id": request.POST.get("courseid"),
                                                             "course_name": request.POST.get('name'),
                                                             "course_term": request.POST.get('term')})
                if status is False:
                    raise Exception("Course not created")
                return render(request, 'coursemanagement.html', {'course_message': 'Course Created Successfully'})
            except Exception as e:
                return render(request, 'coursemanagement.html', {'course_message': 'Course Creation Failed', 'error': str(e)})
        elif request.POST.get('createcoursesection') == "true":
            try:
                status = functions.CourseSection_func.Create(self, {"section_id": request.POST.get('sectionid'),
                                                                    "course": request.POST.get('course'),
                                                                    "section_number": request.POST.get('sectionnumber'),
                                                                    "Time": request.POST.get('time'),
                                                                    "Location": request.POST.get('location'),
                                                                    "credits": request.POST.get('credits'),
                                                                    "instructor": request.POST.get('instructor')})
                if status is False:
                    raise Exception("Course Section not created")
                return render(request, 'coursemanagement.html', {'course_section_message': 'Course Section Created Successfully'})
            except Exception as e:
                return render(request, 'coursemanagement.html',
                              {'course_section_message': 'Course Section Creation Failed', 'error': str(e)})
        elif request.POST.get('createlabsection') == "true":
            try:
                status = functions.LabSection_func.Create(self, {"section_id": request.POST.get('sectionid'),
                                                                 "section_number": request.POST.get('sectionnumber'),
                                                                 "course": request.POST.get('course'),
                                                                 "course_section": request.POST.get('coursesection'),
                                                                 "Time": request.POST.get('time'),
                                                                 "Location": request.POST.get('location'),
                                                                 "Type": request.POST.get('role'),
                                                                 "ta": request.POST.get('ta')})
                if status is False:
                    raise Exception("Lab Section not created")
                return render(request, 'coursemanagement.html', {'lab_message': 'Lab Section Created Successfully'})
            except Exception as e:
                return render(request, 'coursemanagement.html',
                              {'lab_message': 'Lab Section Creation Failed', 'error': str(e)})
        elif request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')
        else:
            return render(request, 'coursemanagement.html', {'message': 'No Course Function Selected'})



class ViewCourses(View):
    def get(self, request):
        if request.session.get('username'):
            courses = functions.Course_func.get_all(self)
            course_sections = functions.CourseSection_func.get_all(self)
            lab_sections = functions.LabSection_func.get_all(self)
            return render(request, 'viewcourses.html',
                          {'courses': courses, 'course_sections': course_sections, 'lab_sections': lab_sections})
        else:
            return redirect('/')

    def post(self, request):
        logout(request)
        return redirect('/')



class ViewUsers(View):
    def get(self, request):
        if request.session.get('username'):
            users = User.objects.all()
            return render(request, 'viewusers.html', {'users': users})
        else:
            return redirect('/')

    def post(self, request):
        logout(request)
        return redirect('/')


class AssignUsers(View):
    def get(self, request):
        return render(request, 'assignusers.html')


class EditContactInfo(View):
    def get(self, request):

        user = functions.User_func.get(self, "username", request.session.get('username'))

        print(user)

        return render(request, 'editcontactinfo.html', {'oldemail': user[0]['email'], 'oldphone':user[0]['phone_number'], 'oldaddress':user[0]['address']})

    def post(self, request):



        try:

            data = {
                'username': request.session.get('username'),
                'email': request.POST.get('email'),
                'phone_number': request.POST.get('phone'),
                'address': request.POST.get('address')
            }



            status = functions.User_func.Edit(self, data)



            if status is False:
                raise Exception("Error while editing contact info")

            user = functions.User_func.get(self,"username", request.session.get('username'))



            return render(request, 'editcontactinfo.html', {'message': "You have successfully edited your contact information", 'oldemail': user[0]['email'], 'oldphone':user[0]['phone_number'], 'oldaddress':user[0]['address']})
        except Exception as e:
            return render(request, 'editcontactinfo.html', {'message': e})


class Notifications(View):
    def get(self, request):
        return render(request, 'notifications.html')


class InstructorDashboard(View):
    def get(self, request):
        if not request.session.get('username') == "":
            return render(request, 'instructor_dashboard.html', {})
        else:
            return redirect('/')

    def post(self, request):
        request.session["username"] = ""
        return redirect('/')

class instructor_edit_contact(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'instructor_edit_contact.html', {})
        else:
            return redirect('/')

    def post(self, request):
        logout(request)
        return redirect('/')

class instructor_section_management(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'instructor_section_management.html', {})
        else:
            return redirect('/')

    def post(self, request):
        logout(request)
        return redirect('/')

class instructor_view_courses(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'instructor_view_courses.html', {})
        else:
            return redirect('/')

    def post(self, request):
        logout(request)
        return redirect('/')

class instructor_view_users(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'instructor_view_users.html', {})
        else:
            return redirect('/')

    def post(self, request):
        logout(request)
        return redirect('/')

class instructor_notifications(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'instructor_notifications.html', {})
        else:
            return redirect('/')

    def post(self, request):
        logout(request)
        return redirect('/')

class TADashboard(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'ta_dashboard.html', {})
        else:
            return redirect('/')

    def post(self, request):
        logout(request)
        return redirect('/')

class ta_edit_contact(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'ta_edit_contact.html', {})
        else:
            return redirect('/')

    def post(self, request):
        logout(request)
        return redirect('/')

class ta_my_sections(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'ta_my_sections.html', {})
        else:
            return redirect('/')

    def post(self, request):
        logout(request)
        return redirect('/')

class ta_view_courses(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'ta_view_courses.html', {})
        else:
            return redirect('/')

    def post(self, request):
        logout(request)
        return redirect('/')

class ta_view_users(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'ta_view_users.html', {})
        else:
            return redirect('/')

    def post(self, request):
        logout(request)
        return redirect('/')
