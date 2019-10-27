from django.contrib import admin

# Register your models here.

from .models import ReminderDB, Profile

admin.site.register(ReminderDB)
admin.site.register(Profile)