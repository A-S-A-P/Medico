from django.db import models

# Create your models here.

class Reminder(models.Model):
        med_name = models.TextField()
        hour = models.TextField()
        minute = models.TimeField()
        PM = models.BooleanField()
        