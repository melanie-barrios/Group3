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

    def Create(self, info: dict) -> bool:
        """
        Create - Creates user based on provided data

        Preconditions: Valid dictionary with correct values based on user.
        Postconditions: User is successfully added to the database.
        Side Effects: Adds a user to database and all locations that reference users.
        In: info is a dictionary containing user information.
        Out: Boolean to determine if operation was accomplished or not.
        """

    def Edit(self, info: dict) -> bool:
        """
        Edit - Updates user information with the provided data.

        Preconditions: User must be authenticated and exist in the database.
        Postconditions: User information is updated in the database if successful.
        Side Effects: May modify user information in the database and anywhere where user is referenced.
        In: info is a dictionary containing user information.
        Out: Boolean to determine if operation was accomplished or not.
        """

    def Delete(self, identity: str) -> bool:
        """
        Delete - Deletes the user from the database.

        Preconditions: User must exist in the database.
        Postconditions: user is removed from the database and everywhere referenced if successful.
        Side Effects: Removed from any database tables as a foreign key.
        In: String to locate the given user by username to delete.
        Out: Boolean to determine if operation was accomplished or not.
        """

    def get(self, query: str, identity: str) -> list:
        """
        get - Retrieves information about the user(s).

        Preconditions: User(s) must be authenticated and exist in the database.
        Postconditions: Returns a list of dictionaries containing user information (user_id, username, email, role_id, is_active).
        Side Effects: none
        In: query string field to search based off of, identity fields value to search for
        Out: List of dictionaries containing the given query
        """

    def get_all(self) -> list:
        """
        get_all - Retrieves all users from the database.

        Preconditions: None.
        Postconditions: Returns a list containing dictionaries of user information.
        Side Effects: None.
        In: None
        Out: List of dictionaries containing all users.
        """


class Course_func(Change, Getting):
    def Create(self, info: dict) -> bool:
        """
        Create - Creates course based on provided data

        Preconditions: Valid dictionary with correct values based on course.
        Postconditions: Course is successfully added to the database.
        Side Effects: Adds a course to database and all locations that reference courses.
        In: info is a dictionary containing course information.
        Out: Boolean to determine if operation was accomplished or not.
        """

    def Edit(self, info: dict) -> bool:
        """
        Edit - Updates course information with the provided data.

        Preconditions: Course must be authenticated and exist in the database.
        Postconditions: Course information is updated in the database if successful.
        Side Effects: May modify user information in the database and anywhere where Course is referenced.
        In: info is a dictionary containing Course information.
        Out: Boolean to determine if operation was accomplished or not.
        """

    def Delete(self, identity: str) -> bool:
        """
        Delete - Deletes the Course from the database.

        Preconditions: Course must exist in the database.
        Postconditions: Course is removed from the database and everywhere referenced if successful.
        Side Effects: Removed from any database tables as a foreign key.
        In: String to locate the given Course by username to delete.
        Out: Boolean to determine if operation was accomplished or not.
        """

    def get(self, query: str, identity: str) -> list:
        """
        get - Retrieves information about the Course(s).

        Preconditions: Course(s) must be authenticated and exist in the database.
        Postconditions: Returns a list of dictionaries containing Course information.
        Side Effects: none
        In: query string field to search based off of, identity fields value to search for
        Out: List of dictionaries containing the given query
        """

    def get_all(self) -> list:
        """
        get_all - Retrieves all Courses from the database.

        Preconditions: None.
        Postconditions: Returns a list containing dictionaries of Course information.
        Side Effects: None.
        In: None
        Out: List of dictionaries containing all Courses.
        """


class CourseSection_func(Change, Getting):
    """
        Create - Creates CourseSection based on provided data

        Preconditions: Valid dictionary with correct values based on CourseSection.
        Postconditions: CourseSection is successfully added to the database.
        Side Effects: Adds a CourseSection to database and all locations that reference CourseSections.
        In: info is a dictionary containing CourseSection information.
        Out: Boolean to determine if operation was accomplished or not.
    """
    def Create(self, info: dict) -> bool:
        # Check if input is empty
        if not info:
            return False

        # Check if all required fields are present
        required_fields = ['section_id', 'course', 'section_number', 'Time', 'Location', 'credits', 'instructor']
        if not all(field in info for field in required_fields):
            return False

        # Check if course section with the given section ID already exists
        if CourseSection.objects.filter(section_id=info['section_id']).exists():
            return False

        # Create and save the new course section
        course_section = CourseSection(section_id=info['section_id'], section_number=info['section_number'],
                                       course=info['course'], Time=info['Time'], Location=info['Location'],
                                       credits=info['credits'], instructor=info['instructor'])
        course_section.save()
        return True

    """
        Edit - Updates CourseSection information with the provided data.

        Preconditions: CourseSection must be authenticated and exist in the database.
        Postconditions: CourseSection information is updated in the database if successful.
        Side Effects: May modify user information in the database and anywhere where CourseSection is referenced.
        In: info is a dictionary containing CourseSection information.
        Out: Boolean to determine if operation was accomplished or not.
    """
    def Edit(self, info: dict) -> bool:
        try:
            # Attempt to retrieve the course section from the database
            course_section = CourseSection.objects.get(section_id=info['section_id'])
            # Update the course section attributes with the provided data
            for key, value in info.items():
                if key == 'instructor':
                    # If the key is 'instructor', retrieve the user object from the database
                    instructor = User.objects.get(username=value)
                    # Set the instructor attribute of the course section to the retrieved user object
                    setattr(course_section, key, instructor)
                else:
                    # Set the attribute of the course section to the provided value
                    setattr(course_section, key, value)
            # Save the updated course section
            course_section.save()
            return True
        except ObjectDoesNotExist:
            # If the course section does not exist in the database, return False
            return False

    """
        Delete - Deletes the CourseSection from the database.

        Preconditions: CourseSection must exist in the database.
        Postconditions: CourseSection is removed from the database and everywhere referenced if successful.
        Side Effects: Removed from any database tables as a foreign key.
        In: String to locate the given CourseSection by section_id to delete.
        Out: Boolean to determine if operation was accomplished or not.
    """
    def Delete(self, identity: str) -> bool:
        try:
            # Attempt to retrieve the course section from the database
            course_section = CourseSection.objects.get(section_id=identity)

            # Delete the retrieved course section
            course_section.delete()

            # Return True to indicate successful deletion
            return True
        except ObjectDoesNotExist:
            # If the course section does not exist in the database, return False
            return False

    """
        get - Retrieves information about the CourseSection(s).

        Preconditions: CourseSection(s) must be authenticated and exist in the database.
        Postconditions: Returns a list of dictionaries containing CourseSection information.
        Side Effects: none
        In: query string field to search based off of, identity fields value to search for
        Out: List of dictionaries containing the given query
    """
    def get(self, query: str, identity: str) -> list:
        # Check if the query is for section_id
        if query == 'section_id':
            try:
                # Attempt to retrieve the course section from the database using its section_id
                course_section = CourseSection.objects.get(section_id=identity)

                # Construct a dictionary containing the course section information
                result = {
                    'section_id': course_section.section_id,
                    'section_number': course_section.section_number,
                    'course': course_section.course.course_id,
                    'Time': course_section.Time,
                    'Location': course_section.Location,
                    'credits': course_section.credits,
                    'instructor': course_section.instructor.name
                }

                # Return a list containing the constructed dictionary
                return [result]
            except ObjectDoesNotExist:
                # If the course section with the provided section_id does not exist in the database,return an empty list
                return []
        else:
            # If the query is not for section_id, return an empty list
            return []

    """
        get_all - Retrieves all CourseSections from the database.

        Preconditions: None.
        Postconditions: Returns a list containing dictionaries of CourseSection information.
        Side Effects: None.
        In: None
        Out: List of dictionaries containing all CourseSections.
    """
    def get_all(self) -> list:
        # Retrieve all course sections from the database
        course_sections = CourseSection.objects.all()

        # Initialize an empty list to store the results
        results = []

        # Iterate over each course section
        for course_section in course_sections:
            # Construct a dictionary containing the course section information
            result = {
                'section_id': course_section.section_id,
                'section_number': course_section.section_number,
                'course': course_section.course.course_id,
                'Time': course_section.Time,
                'Location': course_section.Location,
                'credits': course_section.credits,
                'instructor': course_section.instructor.name
            }

            # Append the constructed dictionary to the results list
            results.append(result)

        # Return the list of results
        return results


class LabSection_func(Change, Getting):
    """
        Create - Creates LabSection based on provided data

        Preconditions: Valid dictionary with correct values based on LabSection.
        Postconditions: LabSection is successfully added to the database.
        Side Effects: Adds a LabSection to database and all locations that reference LabSections.
        In: info is a dictionary containing user information.
        Out: Boolean to determine if operation was accomplished or not.
    """
    def Create(self, info: dict) -> bool:
        # Check if input is empty
        if not info:
            return False

        # Check if all required fields are present
        required_fields = ['section_id', 'course', 'section_number', 'Time', 'Location', 'Type', 'ta', 'course_section']
        if not all(field in info for field in required_fields):
            return False

        # Check if lab section with the given section ID already exists
        if LabSection.objects.filter(section_id=info['section_id']).exists():
            return False

        # Create and save the new lab section
        lab_section = LabSection(section_id=info['section_id'], section_number=info['section_number'],
                                 course_section=info['course_section'], course=info['course'], Time=info['Time'],
                                 Location=info['Location'], Type=info['Type'], ta=info['ta'])
        lab_section.save()
        return True

    """
        Edit - Updates LabSection information with the provided data.

        Preconditions: LabSection must be authenticated and exist in the database.
        Postconditions: LabSection information is updated in the database if successful.
        Side Effects: May modify user information in the database and anywhere where LabSection is referenced.
        In: info is a dictionary containing LabSection information.
        Out: Boolean to determine if operation was accomplished or not.
    """
    def Edit(self, info: dict) -> bool:
        try:
            # Attempt to retrieve the lab section from the database using its section_id
            lab_section = LabSection.objects.get(section_id=info['section_id'])

            # Iterate over each key-value pair in the info dictionary
            for key, value in info.items():
                # Check if the key is 'ta'
                if key == 'ta':
                    # If key is 'ta', retrieve the User object using the provided username and set it as the value
                    ta = User.objects.get(username=value)
                    setattr(lab_section, key, ta)
                else:
                    # For other keys, set the corresponding attribute of lab_section to the provided value
                    setattr(lab_section, key, value)

            # Save the updated lab section
            lab_section.save()

            # Return True to indicate successful editing
            return True
        except ObjectDoesNotExist:
            # If the lab section with the provided section_id does not exist in the database, return False
            return False

    """
        Delete - Deletes the LabSection from the database.

        Preconditions: LabSection must exist in the database.
        Postconditions: LabSection is removed from the database and everywhere referenced if successful.
        Side Effects: Removed from any database tables as a foreign key.
        In: String to locate the given LabSection by username to delete.
        Out: Boolean to determine if operation was accomplished or not.
    """
    def Delete(self, identity: str) -> bool:
        try:
            # Attempt to retrieve the lab section from the database using its section_id
            lab_section = LabSection.objects.get(section_id=identity)

            # Delete the retrieved lab section from the database
            lab_section.delete()

            # Return True to indicate successful deletion
            return True
        except ObjectDoesNotExist:
            # If the lab section with the provided section_id does not exist in the database, return False
            return False

    """
        get - Retrieves information about the LabSection(s).
    
        Preconditions: LabSection(s) must be authenticated and exist in the database.
        Postconditions: Returns a list of dictionaries containing LabSection information.
        Side Effects: none
        In: query string field to search based off of, identity fields value to search for
        Out: List of dictionaries containing the given query
    """
    def get(self, query: str, identity: str) -> list:
        # Check if the query is for section_id
        if query == 'section_id':
            try:
                # Attempt to retrieve the lab section from the database using its section_id
                lab_section = LabSection.objects.get(section_id=identity)

                # Convert the LabSection instance to a dictionary
                result = {
                    'section_id': lab_section.section_id,
                    'section_number': lab_section.section_number,
                    'course_section': lab_section.course_section.section_number,
                    'course': lab_section.course.course_id,
                    'Time': lab_section.Time,
                    'Location': lab_section.Location,
                    'Type': lab_section.Type,
                    'ta': lab_section.ta.name
                }

                # Return a list containing the constructed dictionary
                return [result]
            except ObjectDoesNotExist:
                # If the lab section with the provided section_id does not exist in the database, return an empty list
                return []
        else:
            # If the query is not for section_id, return an empty list
            return []

    """
        get_all - Retrieves all LabSections from the database.

        Preconditions: None.
        Postconditions: Returns a list containing dictionaries of LabSection information.
        Side Effects: None.
        In: None
        Out: List of dictionaries containing all LabSections.
    """
    def get_all(self) -> list:
        # Retrieve all lab sections from the database
        lab_sections = LabSection.objects.all()

        # Initialize an empty list to store the results
        results = []

        # Iterate over each lab section retrieved from the database
        for lab_section in lab_sections:
            # Convert the lab section instance to a dictionary and append it to the results list
            result = {
                'section_id': lab_section.section_id,
                'section_number': lab_section.section_number,
                'course_section': lab_section.course_section.section_number,
                'course': lab_section.course.course_id,
                'Time': lab_section.Time,
                'Location': lab_section.Location,
                'Type': lab_section.Type,
                'ta': lab_section.ta.name
            }
            results.append(result)

        # Return the list of dictionaries containing information about all lab sections
        return results
