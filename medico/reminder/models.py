from django.db import models

# Create your models here.


class Reminder(models.Model):
        # user_name = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
        med_name = models.TextField()
        hour = models.PositiveIntegerField()
        minute = models.PositiveIntegerField()
        PM = models.BooleanField()
        repeat = models.PositiveIntegerField()
        