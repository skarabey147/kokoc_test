from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import *

app_name = 'users'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path('profile/', profile, name='profile'),
    path('list_users/', list_of_users, name='list')]
