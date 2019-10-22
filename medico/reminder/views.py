from django.shortcuts import render
from .forms import ReminderForm, ReminderDBForm
from .models import ReminderDB
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def reminder_view(request):
    print("REMINDER")
    form = ReminderDBForm(request.POST or None)
    if form.is_valid():
        print("Data: ", form.cleaned_data)
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()

    context = {
        "user_id": "Sandy",
        "form": form
        }
    return render(request, "reminder.html", context)
