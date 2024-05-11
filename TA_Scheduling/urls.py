"""
URL configuration for TA_Scheduling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from TA_APP.views import (
    Login, HomePage, AccountManagement, CourseManagement, ViewUsers, ViewCourses, AssignUsers, Notifications,
    EditContactInfo, InstructorDashboard, instructor_edit_contact, instructor_section_management,
    instructor_view_courses, instructor_view_users, instructor_notifications,
    TADashboard, ta_edit_contact, ta_my_sections, ta_view_courses, ta_view_users
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login.as_view()),
    path('homepage/',HomePage.as_view()),
    path('account-management/', AccountManagement.as_view(), name='accountmanagement'),
    path('course-management/', CourseManagement.as_view(), name='coursemanagement'),
    path('view-courses/', ViewCourses.as_view(), name='viewcourses'),
    path('view-users/', ViewUsers.as_view(), name='viewusers'),
    path('assign-users/', AssignUsers.as_view(), name='assignusers'),
    path('notifications/', Notifications.as_view(), name='notifications'),
    path('editcontactinfo/', EditContactInfo.as_view(), name='editcontactinfo'),

    # Instructor Dashboard URL
    path('instructor/dashboard/', InstructorDashboard.as_view(), name='instructor_dashboard'),
    path('instructor/edit_contact/', instructor_edit_contact, name='instructor_edit_contact'),
    path('instructor/section_management/', instructor_section_management, name='instructor_section_management'),
    path('instructor/view_courses/', instructor_view_courses, name='instructor_view_courses'),
    path('instructor/view_users/', instructor_view_users, name='instructor_view_users'),
    path('instructor/notifications/', instructor_notifications, name='instructor_notifications'),

    # TA Dashboard URL
    path('ta/dashboard/', TADashboard.as_view(), name='ta_dashboard'),
    path('ta/edit_contact/', ta_edit_contact, name='ta_edit_contact'),
    path('ta/my_sections/', ta_my_sections, name='ta_my_sections'),
    path('ta/view_courses/', ta_view_courses, name='ta_view_courses'),
    path('ta/view_users/', ta_view_users, name='ta_view_users'),
]
