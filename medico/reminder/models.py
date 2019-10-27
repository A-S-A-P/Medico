from django.db import models
from django.conf import settings
from django.utils.timezone import activate

from django.contrib.auth.models import User

# Create your models here.
#pip install phone-number-field

USER = settings.AUTH_USER_MODEL

# Create your models here.

class ReminderDB(models.Model):  #reminderdb_set -> query
       
        user = models.ForeignKey(USER , default=1, on_delete=models.CASCADE)
        name = models.CharField(max_length=255)
        hour = models.TimeField()
        repeat = models.PositiveIntegerField()
        


        

class Profile(models.Model):
        user = models.ForeignKey(USER , default=1, on_delete=models.CASCADE)
        phone = models.PositiveIntegerField()
        # timezone = TimeZoneField(default='Asia/Kolkata')










