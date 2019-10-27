from django import forms
from .models import ReminderDB, Profile

class ReminderForm(forms.Form):
    name = forms.CharField()
    hour = forms.TimeField()
    repeat = forms.IntegerField()


class ReminderDBForm(forms.ModelForm):
    class Meta:
        model = ReminderDB
        fields = [
            'name', 
            'hour',
            'repeat'
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phone'
        ]
