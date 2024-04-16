from django.db import models



class Instructor(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    instructor_id =  models.IntegerField()

class TA(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
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

    def get_user_info(self) -> dict:
        """
        Retrieves information about the user.

        Preconditions: User must be authenticated and exist in the database.
        Postconditions: Returns a dictionary containing user information (user_id, username, email, role_id, is_active).
        Side Effects: None.
        Parameter Usage: None.
        """

    def update_user_info(self, info: dict) -> bool:
        """
        Updates user information with the provided data.

        Preconditions: User must be authenticated and exist in the database.
        Postconditions: User information is updated in the database if successful.
        Side Effects: May modify user information in the database.
        Parameter Usage: info is a dictionary containing updated user information.
        """

    def authenticate(self, username: str, password: str) -> bool:
        """
        Authenticates user login credentials.

        Preconditions: None.
        Postconditions: Returns True if authentication is successful, False otherwise.
        Side Effects: None.
        Parameter Usage: username and password are strings representing user credentials.
        """


class Course(models.Model):
    """
    Represents a course in the system.
    """

    course_id = models.CharField(primary_key=True)
    course_name = models.CharField(max_length=120)
    course_code = models.IntegerField()
    instructor_id = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    lab_id = models.IntegerField()

    def get_course_info(self) -> dict:
        """
        Retrieves information about the course.

        Preconditions: Course must exist in the database.
        Postconditions: Returns a dictionary containing course information (course_id, course_name, course_code).
        Side Effects: None.
        Parameter Usage: None.
        """

    def update_course_info(self, info: dict) -> bool:
        """
        Updates course information with the provided data.

        Preconditions: Course must exist in the database.
        Postconditions: Course information is updated in the database if successful.
        Side Effects: May modify course information in the database.
        Parameter Usage: info is a dictionary containing updated course information.
        """

    def delete_course(self) -> bool:
        """
        Deletes the course from the database.

        Preconditions: Course must exist in the database.
        Postconditions: Course is removed from the database if successful.
        Side Effects: May delete associated lab sections and TA assignments.
        Parameter Usage: None..
        """


class LabSection(models.Model):
    """
    Represents a lab section in the system.
    """

    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    course_code = models.ForeignKey(Courses, on_delete=models.CASCADE)
    lab_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    ta_id = models.ForeignKey(TA, on_delete=models.CASCADE)

    def get_lab_section_info(self) -> dict:
        """
        Retrieves information about the lab section.

        Preconditions: Lab section must exist in the database.
        Postconditions: Returns a dictionary containing lab section information (labsection_id, course_id, section_number).
        Side Effects: None.
        Parameter Usage: None.
        """

    def update_lab_section_info(self, info: dict) -> bool:
        """
        Updates lab section information with the provided data.

        Preconditions: Lab section must exist in the database.
        Postconditions: Lab section information is updated in the database if successful.
        Side Effects: May modify lab section information in the database.
        Parameter Usage: info is a dictionary containing updated lab section information.
        """

    def delete_lab_section(self) -> bool:
        """
        Deletes the lab section from the database.

        Preconditions: Lab section must exist in the database.
        Postconditions: Lab section is removed from the database if successful.
        Side Effects: May delete associated TA assignments.
        Parameter Usage: None.
        """


class TAAssignment:
    """
    Represents a TA assignment in the system.
    """

    def get_ta_assignment_info(self) -> dict:
        """
        Retrieves information about the TA assignment.

        Preconditions: TA assignment must exist in the database.
        Postconditions: Returns a dictionary containing TA assignment information (taassignment_id, ta_id, labsection_id).
        Side Effects: None.
        Parameter Usage: None.
        """

    def update_ta_assignment_info(self, info: dict) -> bool:
        """
        Updates TA assignment information with the provided data.

        Preconditions: TA assignment must exist in the database.
        Postconditions: TA assignment information is updated in the database if successful.
        Side Effects: May modify TA assignment information in the database.
        Parameter Usage: info is a dictionary containing updated TA assignment information.
        """

    def delete_ta_assignment(self) -> bool:
        """
        Deletes the TA assignment from the database.

        Preconditions: TA assignment must exist in the database.
        Postconditions: TA assignment is removed from the database if successful.
        Side Effects: None.
        Parameter Usage: None.
        """