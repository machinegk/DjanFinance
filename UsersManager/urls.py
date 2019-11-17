from django.urls import path
from .views import login, register

urlpatterns = [
    path('register/', register, name='register-page'),
    path('login/', login, name='login-page'),
]