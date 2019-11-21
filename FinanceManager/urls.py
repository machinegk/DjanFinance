from django.urls import path
from .views import profile, home
urlpatterns = [
    path('home/', home, name='home-page'),
    path('profile/', profile, name='profile-page'),
]