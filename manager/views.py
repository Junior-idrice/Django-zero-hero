from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Post,Profile,Comment,User
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.hashers import make_password
import itertools


# Create your views here.

def index(request):
    return render(request,"manager/index.html")

def verifyInput(username,password):
    error = []
    if len(username) < 4:
        error.append("Username should be atleast four characters")
    elif len(password)<8:
        error.append('password should be atleast eight characters')
    else:
        print("perfect")
    return error

def registerUser(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        hashed_password = make_password(password)

        error =verifyInput(username, password)
        if len(error) != 0:
            error = error[0]
            print(error)
            return render(request, 'manager/registration_form.html',{
                "error":error
            })
        else:
         a = User(username=username, email=email, password=password)
         a.save()
         messages.success(request, "Account was created Successfully")
         return redirect('register')