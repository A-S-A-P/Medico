from django.shortcuts import render
from .forms import ReminderForm

# Create your views here.


def reminder_view(request):
    print("REMINDER")
    form = ReminderForm(request.POST or None)
    if form.is_valid():
        print("Data: ", form.cleaned_data)


    context = {
        "user_id": "Sandy",
        "form": form
        }
    return render(request, "reminder.html", context)
