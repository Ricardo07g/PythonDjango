from django.template.backends import django
from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'accounts:login'}, name='logout')
]