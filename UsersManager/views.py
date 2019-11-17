from django.shortcuts import render, redirect
from django.forms import forms
from django.contrib.auth import authenticate
from .forms import RegistrationForm, LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome-page')
    else:
        form = LoginForm()

    return render(request, 'UsersManager/login.html', {'form' : form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome-page')
    else:
        form = RegistrationForm()
    return render (request, 'UsersManager/register.html', {'form' : form})