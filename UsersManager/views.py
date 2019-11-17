from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

def login(request):
    return render(request, 'UsersManager/login.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome-page')
    else:
        form = RegistrationForm()
    return render (request, 'UsersManager/register.html', {'form' : form})