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
        verify = functions.Login.authenticate(self, str(username), str(password))

        """If user is valid move to home page"""
        if verify == 'S':  # Supervisor (or Administrator)
            request.session['username'] = username
            return render(request, 'homepage.html', {})
        elif verify == 'I':  # Instructor
            request.session['username'] = username
            return redirect('instructor_dashboard')
        elif verify == 'T':  # TA
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
                identity = request.POST.get('delusername')
                functions.User_func.Delete(self, identity)
                return render(request, 'accountmanagement.html', {'delete_message': 'Account Deleted Successfully'})
            except Exception as e:
                return render(request, 'accountmanagement.html',
                              {'delete_message': 'Account Deletion Failed', 'error': str(e)})
        elif request.POST.get('status') == "create":
            try:
                status = functions.User_func.Create(self, {"username": request.POST.get('username'),
                                                           "password": request.POST.get('password'),
                                                           "email": request.POST.get('email'),
                                                           "name": request.POST.get('name'),
                                                           "phone_number": request.POST.get('phone'),
                                                           "address": request.POST.get('address'),
                                                           "type": request.POST.get('role'),
                                                           "skills": ''})
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
            return render(request, 'coursemanagement.html')
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
                return render(request, 'coursemanagement.html',
                              {'course_message': 'Course Creation Failed', 'error': str(e)})
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
                return render(request, 'coursemanagement.html',
                              {'course_section_message': 'Course Section Created Successfully'})
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
        names = User.objects.values_list('name', flat=True)
        courses = Course.objects.all()
        section_ids = CourseSection.objects.values_list('section_id', flat=True)
        section_numbers = CourseSection.objects.values_list('section_number', flat=True)

        context = {
            'names': names,
            'courses': courses,
            'section_ids': section_ids,
            'section_numbers': section_numbers,
        }
        return render(request, 'assignusers.html', context)

    def post(self, request):
        if request.POST.get('assignuser') == 'true':
            name = request.POST.get('names')
            course_id = request.POST.get('courseid')
            section_id = request.POST.get('sectionid')
            section_number = request.POST.get('sectionnumber')

            try:
                user = User.objects.get(name=name)
                course = Course.objects.get(course_id=course_id)
                # Assuming CourseSection model has 'section_number' field, you can adjust accordingly
                section = course.coursesection_set.get(section_id=section_id, section_number=section_number)

                # Assign user to the course section
                section.instructor = user
                section.save()

                # Optionally, you can redirect to a success page or render a success message
                return render(request, 'assignusers.html', {'message': 'User assigned Successfully'})
            except Exception as e:
                # Handle if user or course doesn't exist
                return render(request, 'assignusers.html', {'message': 'User or Course not found.'})
        elif request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')


class EditContactInfo(View):
    def get(self, request):
        return render(request, 'editcontactinfo.html')

    def post(self, request):
        if request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')


class Notifications(View):
    def get(self, request):
        return render(request, 'notifications.html')

    def post(self, request):
        if request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')


class InstructorDashboard(View):
    def get(self, request):
        if not request.session.get('username') == "":
            return render(request, 'instructor_dashboard.html', {})
        else:
            return redirect('/')

    def post(self, request):
        if request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')


class instructor_edit_contact(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'instructor_edit_contact.html', {})
        else:
            return redirect('/')

    def post(self, request):
        if request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')


class instructor_section_management(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'instructor_section_management.html', {})
        else:
            return redirect('/')

    def post(self, request):
        if request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')


class instructor_view_courses(View):
    def get(self, request):
        if request.session.get('username'):
            courses = functions.Course_func.get_all(self)
            course_sections = functions.CourseSection_func.get_all(self)
            lab_sections = functions.LabSection_func.get_all(self)
            return render(request, 'instructor_view_courses.html',
                          {'courses': courses, 'course_sections': course_sections, 'lab_sections': lab_sections})
        else:
            return redirect('/')

    def post(self, request):
        if request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')


class instructor_view_users(View):
    def get(self, request):
        if request.session.get('username'):
            users = User.objects.all()
            return render(request, 'instructor_view_users.html', {'users': users})
        else:
            return redirect('/')

    def post(self, request):
        if request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')


class instructor_notifications(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'instructor_notifications.html', {})
        else:
            return redirect('/')

    def post(self, request):
        if request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')


class TADashboard(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'ta_dashboard.html', {})
        else:
            return redirect('/')

    def post(self, request):
        if request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')


class ta_edit_contact(View):
    def get(self, request):
        if request.session.get('username'):
            return render(request, 'ta_edit_contact.html', {})
        else:
            return redirect('/')

    def post(self, request):
        if request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')


class ta_my_sections(View):
    def get(self, request):
        if request.session.get('username'):
            username = request.session.get('username')
            user = User.objects.get(username=username)
            my_lab_section = functions.LabSection_func.get(self, query='ta', identity=user.id)
            return render(request, 'ta_my_sections.html', {'lab_sections': my_lab_section})
        else:
            return redirect('/')

    def post(self, request):
        if request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')


class ta_view_courses(View):
    def get(self, request):
        if request.session.get('username'):
            courses = functions.Course_func.get_all(self)
            course_sections = functions.CourseSection_func.get_all(self)
            lab_sections = functions.LabSection_func.get_all(self)
            return render(request, 'ta_view_courses.html',
                          {'courses': courses, 'course_sections': course_sections, 'lab_sections': lab_sections})
        else:
            return redirect('/')

    def post(self, request):
        if request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')


class ta_view_users(View):
    def get(self, request):
        if request.session.get('username'):
            users = User.objects.all()
            return render(request, 'ta_view_users.html', {'users': users})
        else:
            return redirect('/')

    def post(self, request):
        if request.POST.get('logout') == "Log out":
            logout(request)
            return redirect('/')
