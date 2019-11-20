from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! Your account has been created! Now you're able to log in!")
            return redirect('login-page')
    else:
        form = RegistrationForm()
    return render (request, 'UsersManager/register.html', {'form' : form})