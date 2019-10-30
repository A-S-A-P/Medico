from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReminderForm, ReminderDBForm, ProfileForm
from .models import ReminderDB, Profile
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from threading import Timer
# Create your views here.

@login_required()
def reminder_view(request):
    print("REMINDER")
    form = ReminderDBForm(request.POST or None)
    if form.is_valid():
        print("Data: ", form.cleaned_data)
        
        obj = form.save(commit=False)
        obj.user = request.user
        current_time =datetime.today()
        reminder_time = current_time.replace( hour=obj.hour.hour, minute=obj.hour.minute ) 
        if(reminder_time < current_time):
            delta_t = timedelta(hours=24) - ( current_time - reminder_time )
        else:
            delta_t = reminder_time - current_time 

        secs = delta_t.total_seconds()
        from .tasks import schedule_reminder
        t = Timer(secs, schedule_reminder, [obj])
        t.start()
        print("Set a new Reminder for ", obj.id)
        obj.save()

    
    Med_list_query = ReminderDB.objects.filter(user=request.user)
    
    

    context = {
        "user_id": request.user.first_name,
        "form": form,
        "med_list": Med_list_query
        }
    return render(request, "reminder.html", context)

@login_required()
def register_phone_view(request):
    row = Profile.objects.filter(user=request.user)
    print(type(row))
    print("PHONE REG")
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        print("VALID")
        print("Data: ", form.cleaned_data)
        if row.exists():
            row.update(phone = form.cleaned_data['phone'])
            print("EXISTS, ", form.cleaned_data['phone'])
        else:
            obj = form.save(commit=False)
            obj.user = request.user
            print("Doesnt exist?", type(obj))
            obj.save()
        return redirect("../")

    return render(request, "register2.html")

