from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home-page'),
    path('profile/', profile, name='profile-page'),
    path('daily/', daily, name='daily-page'),
    path('general-statistics/', general_statistics, name='general-statistics-page'),
    path('income/', income, name='income-page'),
    path('expenses/', expenses, name='expenses-page'),
    path('history/', history, name='history-page'),
    path('profile/', profile, name='profile-page'),
    path('start/', start, name='start-page')
]