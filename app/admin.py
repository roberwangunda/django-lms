from django.contrib import admin
from django.contrib.auth.models import Group

from app.models import *


admin.site.register(Semester)
admin.site.register(Session)
admin.site.register(NewsAndEvents)