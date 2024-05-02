import django
from django.core.exceptions import ObjectDoesNotExist
from abc import ABC, abstractmethod
from .models import User, Course, LabSection, CourseSection


class Change(ABC):
    """Create method for general creation"""

    @abstractmethod
    def Create(self, info: dict):
        pass

    """Edit method for general updating"""

    @abstractmethod
    def Edit(self, info: dict):
        pass

    @abstractmethod
    def Delete(self, identity: str):
        pass


class Getting(ABC):
    """General method for getting based on query"""

    @abstractmethod
    def get(self, query: str, identity: str):
        pass

    """General method for getting all instances"""

    @abstractmethod
    def get_all(self):
        pass


class Login:
    """
    Authenticates user login credentials.

    Preconditions: None.
    Postconditions: Returns True if authentication is successful, False otherwise.
    Side Effects: None.
    Parameter Usage: username and password are strings representing user credentials.
    """

    def authenticate(self, username: str, password: str) -> bool:
        """Check username"""
        try:
            temp_user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return False

        """Check is password matches username"""
        if temp_user.password == password:
            return True
        else:
            return False


class User_func(Change, Getting):
    """
    Create - Creates user based on provided data

    Preconditions: Valid dictionary with correct values based on user.
    Postconditions: User is successfully added to the database.
    Side Effects: Adds a user to database and all locations that reference users.
    In: info is a dictionary containing user information.
    Out: Boolean to determine if operation was accomplished or not.
    """

    def Create(self, info: dict) -> bool:
        """Check for empty dictionaries before querying info"""
        if not bool(info):
            return False

        """Check for empty required values before creation"""
        if not ('username' in info and 'password' in info and 'name' in info
                and 'email' in info and 'phone_number' in info and 'address' in info and 'type' in info):
            return False

        """Take entries from input dictionary and create a new user"""
        if 'skills' in info:
            """Skills is optional field for creation so check if present"""
            user = User(username=info['username'], password=info['password'], name=info['name'],
                        phone_number=info['phone_number'], email=info['email'], address=info['address'],
                        type=info['type'], skills=info['skills'])
        else:
            user = User(username=info['username'], password=info['password'], name=info['name'],
                        phone_number=info['phone_number'], email=info['email'], address=info['address'],
                        type=info['type'])
        user.save()
        return True

    def Edit(self, info: dict) -> bool:
        """
        Edit - Updates user information with the provided data.

        Preconditions: User must be authenticated and exist in the database.
        Postconditions: User information is updated in the database if successful.
        Side Effects: May modify user information in the database and anywhere where user is referenced.
        In: info is a dictionary containing user information.
        Out: Boolean to determine if operation was accomplished or not.
        """

    """
    Delete - Deletes the user from the database.

    Preconditions: User must exist in the database.
    Postconditions: user is removed from the database and everywhere referenced if successful.
    Side Effects: Removed from any database tables as a foreign key.
    In: String to locate the given user by username to delete.
    Out: Boolean to determine if operation was accomplished or not.
    """
    def Delete(self, identity: str) -> bool:
        """Try and find the user"""
        try:
            temp_user = User.objects.get(username=identity)
        except ObjectDoesNotExist:
            return False

        """delete the user"""
        temp_user.delete()
        return True

    def get(self, query: str, identity: str) -> list:
        """
        get - Retrieves information about the user(s).

        Preconditions: User(s) must be authenticated and exist in the database.
        Postconditions: Returns a list of dictionaries containing user information (user_id, username, email, role_id, is_active).
        Side Effects: none
        In: query string field to search based off of, identity fields value to search for
        Out: List of dictionaries containing the given query
        """

    """
    get_all - Retrieves all users from the database.

    Preconditions: None.
    Postconditions: Returns a list containing dictionaries of user information.
    Side Effects: None.
    In: None
    Out: List of dictionaries containing all users.
    """
    def get_all(self) -> list:
        """Get all users in table"""
        user_list = User.objects.all()

        """Initialize user list"""
        return_list = []
        """Add entries to list"""
        for user in user_list:
            """create user dictionary"""
            temp_dic = {'name': user.name, 'username': user.username,
                        'password': user.password, 'email': user.email,
                        'phone_number': int(user.phone_number), 'address': user.address, 'type': user.type, 'skills': user.skills}
            """add to list"""
            return_list.append(temp_dic)
        """return the list of users"""
        return return_list


class Course_func(Change, Getting):
    """
    Create - Creates course based on provided data

    Preconditions: Valid dictionary with correct values based on course.
    Postconditions: Course is successfully added to the database.
    Side Effects: Adds a course to database and all locations that reference courses.
    In: info is a dictionary containing course information.
    Out: Boolean to determine if operation was accomplished or not.
    """
    def Create(self, info: dict) -> bool:
        """Check for empty dictionaries before querying info"""
        if not bool(info):
            return False

        """Check that required fields are present"""
        if not ('course_id' in info and 'course_name' in info and 'course_term' in info):
            return False

        """Add course to database"""
        course = Course(course_id=info['course_id'], course_name=info['course_name'],course_term=info['course_term'])
        course.save()
        return True

    def Edit(self, info: dict) -> bool:
        """
        Edit - Updates course information with the provided data.

        Preconditions: Course must be authenticated and exist in the database.
        Postconditions: Course information is updated in the database if successful.
        Side Effects: May modify user information in the database and anywhere where Course is referenced.
        In: info is a dictionary containing Course information.
        Out: Boolean to determine if operation was accomplished or not.
        """

    """
    Delete - Deletes the Course from the database.

    Preconditions: Course must exist in the database.
    Postconditions: Course is removed from the database and everywhere referenced if successful.
    Side Effects: Removed from any database tables as a foreign key.
    In: String to locate the given Course by username to delete.
    Out: Boolean to determine if operation was accomplished or not.
    """
    def Delete(self, identity: str) -> bool:
        """Try and find the course"""
        try:
            temp_course = Course.objects.get(course_id=identity)
        except ObjectDoesNotExist:
            return False

        """delete the course"""
        temp_course.delete()
        return True

    def get(self, query: str, identity: str) -> list:
        """
        get - Retrieves information about the Course(s).

        Preconditions: Course(s) must be authenticated and exist in the database.
        Postconditions: Returns a list of dictionaries containing Course information.
        Side Effects: none
        In: query string field to search based off of, identity fields value to search for
        Out: List of dictionaries containing the given query
        """

    """
    get_all - Retrieves all Courses from the database.

    Preconditions: None.
    Postconditions: Returns a list containing dictionaries of Course information.
    Side Effects: None.
    In: None
    Out: List of dictionaries containing all Courses.
    """
    def get_all(self) -> list:
        """Get all courses in table"""
        course_list = Course.objects.all()

        """Initialize user list"""
        return_list = []
        """Add entries to list"""
        for course in course_list:
            """create user dictionary"""
            course_sections = course.coursesection_set.all()
            lab_sections = course.labsection_set.all()
            for section in course_sections:
                """Add entry to dictionary"""
            """add to list"""
            return_list.append(temp_dic)
        """return the list of users"""
        return return_list


class CourseSection_func(Change, Getting):
    def Create(self, info: dict) -> bool:
        """
        Create - Creates CourseSection based on provided data

        Preconditions: Valid dictionary with correct values based on CourseSection.
        Postconditions: CourseSection is successfully added to the database.
        Side Effects: Adds a CourseSection to database and all locations that reference CourseSections.
        In: info is a dictionary containing CourseSection information.
        Out: Boolean to determine if operation was accomplished or not.
        """

    def Edit(self, info: dict) -> bool:
        """
        Edit - Updates CourseSection information with the provided data.

        Preconditions: CourseSection must be authenticated and exist in the database.
        Postconditions: CourseSection information is updated in the database if successful.
        Side Effects: May modify user information in the database and anywhere where CourseSection is referenced.
        In: info is a dictionary containing CourseSection information.
        Out: Boolean to determine if operation was accomplished or not.
        """

    def Delete(self, identity: str) -> bool:
        """
        Delete - Deletes the CourseSection from the database.

        Preconditions: CourseSection must exist in the database.
        Postconditions: CourseSection is removed from the database and everywhere referenced if successful.
        Side Effects: Removed from any database tables as a foreign key.
        In: String to locate the given CourseSection by username to delete.
        Out: Boolean to determine if operation was accomplished or not.
        """

    def get(self, query: str, identity: str) -> list:
        """
        get - Retrieves information about the CourseSection(s).

        Preconditions: CourseSection(s) must be authenticated and exist in the database.
        Postconditions: Returns a list of dictionaries containing CourseSection information.
        Side Effects: none
        In: query string field to search based off of, identity fields value to search for
        Out: List of dictionaries containing the given query
        """

    def get_all(self) -> list:
        """
        get_all - Retrieves all CourseSections from the database.

        Preconditions: None.
        Postconditions: Returns a list containing dictionaries of CourseSection information.
        Side Effects: None.
        In: None
        Out: List of dictionaries containing all CourseSections.
        """


class LabSection_func(Change, Getting):
    def Create(self, info: dict) -> bool:
        """
        Create - Creates LabSection based on provided data

        Preconditions: Valid dictionary with correct values based on LabSection.
        Postconditions: LabSection is successfully added to the database.
        Side Effects: Adds a LabSection to database and all locations that reference LabSections.
        In: info is a dictionary containing user information.
        Out: Boolean to determine if operation was accomplished or not.
        """

    def Edit(self, info: dict) -> bool:
        """
        Edit - Updates LabSection information with the provided data.

        Preconditions: LabSection must be authenticated and exist in the database.
        Postconditions: LabSection information is updated in the database if successful.
        Side Effects: May modify user information in the database and anywhere where LabSection is referenced.
        In: info is a dictionary containing LabSection information.
        Out: Boolean to determine if operation was accomplished or not.
        """

    def Delete(self, identity: str) -> bool:
        """
        Delete - Deletes the LabSection from the database.

        Preconditions: LabSection must exist in the database.
        Postconditions: LabSection is removed from the database and everywhere referenced if successful.
        Side Effects: Removed from any database tables as a foreign key.
        In: String to locate the given LabSection by username to delete.
        Out: Boolean to determine if operation was accomplished or not.
        """

    def get(self, query: str, identity: str) -> list:
        """
        get - Retrieves information about the LabSection(s).

        Preconditions: LabSection(s) must be authenticated and exist in the database.
        Postconditions: Returns a list of dictionaries containing LabSection information.
        Side Effects: none
        In: query string field to search based off of, identity fields value to search for
        Out: List of dictionaries containing the given query
        """

    def get_all(self) -> list:
        """
        get_all - Retrieves all LabSections from the database.

        Preconditions: None.
        Postconditions: Returns a list containing dictionaries of LabSection information.
        Side Effects: None.
        In: None
        Out: List of dictionaries containing all LabSections.
        """
