import uuid

from django.db import models


class Instructor(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    instructor_id = models.IntegerField()


class TA(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    ta_id = models.IntegerField(primary_key=True)


class User(models.Model):
    """
    Represents a user in the system.
    """

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField()
    name = models.CharField()
    phone_number = models.CharField(max_length=11)
    address = models.TextField()
    email = models.TextField()


class Course(models.Model):
    """
    Represents a course in the system.
    """

    course_id = models.CharField(primary_key=True)
    course_name = models.CharField(max_length=120)
    course_code = models.IntegerField()
    instructor_id = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    lab_id = models.IntegerField()


class LabSection(models.Model):
    """
    Represents a lab section in the system.
    """

    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    lab_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    ta_id = models.ForeignKey(TA, on_delete=models.CASCADE)
