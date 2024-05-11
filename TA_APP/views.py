from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from .models import User, Course, LabSection, CourseSection
import TA_APP.functions as functions


class Login(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        verify = functions.Login.authenticate(self, str(username), str(password))
        if verify:
            request.session['username'] = username
            return redirect('/homepage/')
        else:
            return render(request, "login.html", {"message": "Username or password is incorrect"})


class HomePage(View):
    def get(self, request):
        username = request.session.get('username')
        if not username:
            return redirect('/')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return redirect('/')

        # Redirect based on the user's role
        if user.type == 'S':  # Supervisor (or Administrator)
            return render(request, 'homepage.html', {})
        elif user.type == 'I':  # Instructor
            return redirect('instructor_dashboard')
        elif user.type == 'T':  # TA
            return redirect('ta_dashboard')
        else:
            return redirect('/')

    def post(self, request):
        request.session["username"] = ""
        return redirect('/')


class AccountManagement(View):
    def get(self, request):
        return render(request, 'accountmanagement.html')

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

        else:
            return render(request, 'accountmanagement.html', {'message': 'No Account Function Selected'})


class CourseManagement(View):
    def get(self, request):
        return render(request, 'coursemanagement.html')

    def post(self, request):

        if request.POST.get('createcourse') == "true":
            try:

                status = functions.Course_func.Create(self, {"course_id": request.POST.get("courseid"),
                                                             "course_name": request.POST.get('name'),
                                                             "course_term": request.POST.get('term')})
                if status is False:
                    raise Exception("Course not created")
                return render(request, 'coursemanagement.html', {'message': 'Course Created Successfully'})
            except Exception as e:
                return render(request, 'coursemanagement.html', {'message': 'Course Creation Failed', 'error': str(e)})
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
                return render(request, 'coursemanagement.html', {'message': 'Course Section Created Successfully'})
            except Exception as e:
                return render(request, 'coursemanagement.html',
                              {'message': 'Course Section Creation Failed', 'error': str(e)})
        else:
            return render(request, 'coursemanagement.html', {'message': 'No Account Function Selected'})


class ViewCourses(View):
    def get(self, request):
        return render(request, 'viewcourses.html')


class ViewUsers(View):
    def get(self, request):
        return render(request, 'viewusers.html')


class AssignUsers(View):
    def get(self, request):
        return render(request, 'assignusers.html')


class EditContactInfo(View):
    def get(self, request):
        return render(request, 'editcontactinfo.html')


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


def instructor_edit_contact(request):
    return render(request, 'instructor_edit_contact.html')


def instructor_section_management(request):
    return render(request, 'instructor_section_management.html')


def instructor_view_courses(request):
    return render(request, 'instructor_view_courses.html')


def instructor_view_users(request):
    return render(request, 'instructor_view_users.html')


def instructor_notifications(request):
    return render(request, 'instructor_notifications.html')


class TADashboard(View):
    def get(self, request):
        if not request.session.get('username') == "":
            return render(request, 'ta_dashboard.html', {})
        else:
            return redirect('/')

    def post(self, request):
        request.session["username"] = ""
        return redirect('/')


def ta_edit_contact(request):
    return render(request, 'ta_edit_contact.html')


def ta_my_sections(request):
    return render(request, 'ta_my_sections.html')


def ta_view_courses(request):
    return render(request, 'ta_view_courses.html')


def ta_view_users(request):
    return render(request, 'ta_view_users.html')
