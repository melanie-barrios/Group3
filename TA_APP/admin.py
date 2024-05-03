
from TA_APP.models import User
from TA_APP.models import Course
from TA_APP.models import LabSection
from TA_APP.models import CourseSection
from django.contrib import admin




admin.site.register(User)
admin.site.register(Course)
admin.site.register(LabSection)
admin.site.register(CourseSection)

