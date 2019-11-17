from django.urls import path
from .views import register, login

urlpatterns = [
    path('register/', register, name='register-page'),
    path('login/', login, name='login-page'),
]