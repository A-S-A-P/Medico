from django import forms

class ReminderForm(forms.Form):
    name = forms.CharField()
    hour = forms.TimeField()
    repeat = forms.IntegerField()
