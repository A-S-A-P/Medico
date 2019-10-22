from django.shortcuts import render, get_object_or_404
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

    
    Med_list_query = ReminderDB.objects.filter(user=request.user)
    
    

    context = {
        "user_id": request.user.first_name,
        "form": form,
        "med_list": Med_list_query
        }
    return render(request, "reminder.html", context)
