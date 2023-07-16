from re import template

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    path('about/', TemplateView.as_view(template_name='home/about.html'), name='about'),
    path('register/', views.register, name='register'),

]

urlpatterns += staticfiles_urlpatterns()
