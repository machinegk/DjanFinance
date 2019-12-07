from django import forms
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import Profile
from django.forms.widgets import ClearableFileInput


class CustomClearableFileInput(ClearableFileInput):
    template_name = "UsersManager/picture_uploader.html"

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control col-lg-8'}))
    first_name = forms.CharField(required=True, max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control col-lg-8'}))
    last_name = forms.CharField(required=True, max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control col-lg-8'}))

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name'
        ]



class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'country',
            'birthday',
            'city',
            'image',
        ]
        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-control', 'id': 'country_selector'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control', 'id': 'datepicker', 'aria-describedby': 'calendar-addon'}),
            'city': forms.TextInput(attrs={'class': 'form-control col-lg-8'}),
            'image' : CustomClearableFileInput,
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'input'}))


class LoginView(views.LoginView):
    form_class = LoginForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input'}), max_length=100)
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input'}))
    first_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name"
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user
