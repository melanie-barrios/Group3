# TA_Scheduling/urls.py
from django.contrib import admin
from django.urls import path
from TA_APP.views import (
    Login, HomePage, AccountManagement, CourseManagement, ViewUsers, ViewCourses,
    InstructorDashboard, instructor_edit_contact, instructor_section_management,
    instructor_view_courses, instructor_view_users, instructor_notifications,
    TADashboard, ta_edit_contact, ta_my_sections, ta_view_courses, ta_view_users
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('homepage/', HomePage.as_view(), name='homepage'),
    path('account-management/', AccountManagement.as_view(), name='accountmanagement'),
    path('course-management/', CourseManagement.as_view(), name='coursemanagement'),
    path('view-courses/', ViewCourses.as_view(), name='viewcourses'),
    path('view-users/', ViewUsers.as_view(), name='viewusers'),

    # Instructor Dashboard URL
    path('instructor/dashboard/', InstructorDashboard.as_view(), name='instructor_dashboard'),
    path('instructor/edit_contact/', instructor_edit_contact.as_view(), name='instructor_edit_contact'),
    path('instructor/section_management/', instructor_section_management.as_view(), name='instructor_section_management'),
    path('instructor/view_courses/', instructor_view_courses.as_view(), name='instructor_view_courses'),
    path('instructor/view_users/', instructor_view_users.as_view(), name='instructor_view_users'),
    path('instructor/notifications/', instructor_notifications.as_view(), name='instructor_notifications'),

    # TA Dashboard URL
    path('ta/dashboard/', TADashboard.as_view(), name='ta_dashboard'),
    path('ta/edit_contact/', ta_edit_contact.as_view(), name='ta_edit_contact'),
    path('ta/my_sections/', ta_my_sections.as_view(), name='ta_my_sections'),
    path('ta/view_courses/', ta_view_courses.as_view(), name='ta_view_courses'),
    path('ta/view_users/', ta_view_users.as_view(), name='ta_view_users'),
]
