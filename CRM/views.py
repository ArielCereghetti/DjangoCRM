from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import RegisterUser, LoginForm
from django.contrib.auth.models import User

from .models import Customer

# Create your views here.
@login_required(login_url="CRM:login")
def index(request):
    

    return render(request, 'CRM/index.html', {'model': Customer().__dict__()})

def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('CRM:index'))

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
        else:
            return render(request, 'CRM/login.html', {"form": form })

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('CRM:index'))
        else:
            return render(request, 'CRM/login.html', {"form": form })
    

    return render(request, 'CRM/login.html', {"form": LoginForm()})

def register_user(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            print(request.POST)
        else:
            return render(request, "CRM/register.html", {
                "form": RegisterUser(),
                "message": "One or more fields were incorrect, please try again"
            })


    return render(request, "CRM/register.html", {
        "form": RegisterUser(),
    })