from django.urls import path
from django.contrib.auth.views import LogoutView
from .forms import LoginView
from .views import register, settings

urlpatterns = [
    path('register/', register, name='register-page'),
    path('login/', LoginView.as_view(template_name='UsersManager/login.html', redirect_authenticated_user=True), name='login-page'),
    path('logout/', LogoutView.as_view(template_name='UsersManager/logout.html'), name='logout-page'),
    path('settings/', settings, name='settings-page'),
]