from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget = forms.TextInput(attrs= { 'class' : 'input'}))
    password = forms.CharField(required=True, widget = forms.PasswordInput(attrs= { 'class' : 'input'}))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, widget = forms.TextInput(attrs= { 'class' : 'input'}), max_length=100)
    email = forms.EmailField(required=True, widget = forms.EmailInput(attrs= { 'class' : 'input'}))
    first_name = forms.CharField(required=True, max_length=100, widget = forms.TextInput(attrs= { 'class' : 'input'}))
    last_name = forms.CharField(required=True, max_length=100, widget = forms.TextInput(attrs= { 'class' : 'input'}))
    password1 = forms.CharField(required=True, widget = forms.PasswordInput(attrs= { 'class' : 'input'}))
    password2 = forms.CharField(required=True, widget = forms.PasswordInput(attrs= { 'class' : 'input'}))

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
