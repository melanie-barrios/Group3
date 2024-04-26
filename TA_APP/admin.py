from TA_APP.models import Instructor
from TA_APP.models import TA
from TA_APP.models import Supervisor
from TA_APP.models import User
from TA_APP.models import Course
from TA_APP.models import LabSection
from django.contrib import admin


admin.site.register(Instructor)
admin.site.register(TA)
admin.site.register(User)
admin.site.register(Supervisor)
admin.site.register(Course)
admin.site.register(LabSection)


