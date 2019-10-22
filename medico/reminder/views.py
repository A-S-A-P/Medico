from django.shortcuts import render

# Create your views here.


def reminder_view(request):
    return render(request, "reminder.html", {"id": "Sandy"})
