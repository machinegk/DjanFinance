from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required


def user_is_not_logged_in(user):
    return not user.is_authenticated


@login_required()
def settings(request):
    return HttpResponse("Settings page")


@user_passes_test(user_is_not_logged_in, redirect_field_name='home-page')
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! Your account has been created! Now you're able to log in!")
            return redirect('login-page')
    else:
        form = RegistrationForm()
    return render(request, 'UsersManager/register.html', {'form': form})
