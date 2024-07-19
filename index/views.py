from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student
from .form import registration_form


# Create your views here.
def home(request):
    return render(request, "index.html")
  
def dept(request):
    return render(request, "department.html")

@login_required(login_url= "/login/") 
def dashboard(request):
    students = Student.objects.all().order_by('-id')
    return render(request, "dashboard.html", {'all':students})

def about(request):
    return render(request, "about.html")



def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
            messages.success(request, ("there was an error"))
            return redirect('login')


    else:
        return render(request, "login.html", {})
    

def logout_user(request):
    logout(request)
    return redirect('home')


def admission(request):
    return render(request, "registration.html")

def insertuser(request):
    # vname = request.POST['name']
    # vage = request.POST['age']
    # vphone = request.POST['phone']
    # vpicture = request.POST['picture']
    # us = Student(name = vname, age = vage, phone = vphone, picture = vpicture)
    # us.save()

    form = registration_form(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
    return redirect('home')
