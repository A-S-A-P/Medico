from django.http import HttpResponse
from django.shortcuts import render

#def home_view(request):
#    return HttpResponse("<h1>Hello WOrld</h1>")



def home_view(request):
    return render(request, "add-medicine.html")
