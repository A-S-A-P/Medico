from django.db import models
from django.conf import settings

# Create your models here.

USER = settings.AUTH_USER_MODEL

class ReminderDB(models.Model):  #reminderdb_set -> query
       
        user = models.ForeignKey(USER , default=1, on_delete=models.CASCADE)
        name = models.CharField(max_length=255)
        hour = models.TimeField()
        repeat = models.PositiveIntegerField()
        