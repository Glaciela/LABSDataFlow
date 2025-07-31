from django.contrib.auth import views as auth_views
from django.urls import path

from .views import DashboardView, IndexView, NewUserView

app_name = 'core'

urlpatterns = [
    path('', IndexView, name='home'),
    path('home/', IndexView, name='home'),
    path('dashboard/', DashboardView, name='dashboard'),
    path('new_user/', NewUserView, name='new_user'),
]