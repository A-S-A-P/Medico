from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from reminder.forms import ProfileForm

#def home_view(request):
#    return HttpResponse("<h1>Hello WOrld</h1>")



def home_view(request):
    return render(request, "user.html")



def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("../")
        else:
            return render(request, "login.html", {'flag': True})
    else:
        return render(request, "login.html")
    #return HttpResponse("<h1>Login First!<h1> <a href='..'> CLick here!</a>  ")





def register_view(request):
    print("register")
    if request.method == "POST":
        print("POSTYES")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password1']
        email= "placeholder@gmail.com"
        phone = request.POST['phone']
        print("phone: " + phone)
        if(len(password) <= 6):

            print("pass too short")
            return render(request, 'register.html', {'pass_flag': True})
        
        try:
            user = User.objects.create_user(
                    username=username, 
                    password=password,
                    email=email,
                    first_name= first_name,
                    last_name=last_name,
                
                )

            user.save()
            print("user created\n")
            auth.login(request, user)
            return redirect("../phone")
        except:
            print("error")
            return render(request, 'register.html', {'alert_flag': True})
          
      


    else:
        print("else_out")
        return render(request, 'register.html')



def logout_view(request):
    auth.logout(request)
    return redirect("../")