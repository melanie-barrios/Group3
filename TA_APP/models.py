import uuid

from django.db import models


class User(models.Model):
    """
    Represents a user in the system.
    """
    """user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)"""
    type = {"S": "Supervisor","I":"Instructor","T":"TA"}
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    name = models.CharField(max_length=75)
    phone_number = models.CharField(max_length=11)
    address = models.TextField()
    email = models.TextField()
    type = models.CharField(max_length=10, choices=type,default="Supervisor")
    skills = models.TextField(blank=True)


class Course(models.Model):
    """
    Represents a course in the system.
    """
    term = {"F":"Fall","W":"Winter","Sp":"Spring","Su":"Summer"}
    course_id = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length=120)
    course_term = models.CharField(max_length=2, choices=term)
    assignments = models.ManyToManyField(User,blank=True)

class CourseSection(models.Model):
    """
    represents a course section in the system
    """
    section_id = models.IntegerField(primary_key=True)
    section_number = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Time = models.TextField()
    Location = models.TextField()
    credits = models.IntegerField()
    instructor = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)

class LabSection(models.Model):
    """
    Represents a lab section in the system.
    """
    type = {"L":"Lab","D":"Discussion","G":"Grader"}
    section_id = models.IntegerField(primary_key=True)
    section_number = models.IntegerField()
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Time = models.TextField()
    Location = models.TextField()
    Type = models.CharField(max_length=10, choices=type,default="Lab")
    ta = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
