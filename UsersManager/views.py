from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import RegistrationForm, UpdateProfileForm, UpdateUserForm
from django.contrib.auth.decorators import user_passes_test, login_required
from datetime import datetime

def user_is_not_logged_in(user):
    return not user.is_authenticated


@login_required()
def settings(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            timestamp = datetime.now().strftime('%H:%M:%S')
            data = {
                'success' : "Your account was updated successfully!",
                'error' : "Error occurred, check your data, please.",
                'timestamp' : timestamp
            }
            return JsonResponse(data)


    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'UsersManager/settings.html', context)


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
