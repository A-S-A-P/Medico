from django.shortcuts import render
from django.contrib.auth.models import User, auth 
# Create your views here.


def register(request):
    print("yes1")
    if request.method == "POST":
        print("yes2")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password1']
        email= "placeholder@gmail.com"
        user = User.objects.create_user(
            username=username, 
            password=password,
            email=email,
            first_name= first_name,
            last_name=last_name
            )
        

    else:
        print("yes3")
        return render(request, 'register.html')

