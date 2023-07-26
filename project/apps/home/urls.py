from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'Home'

urlpatterns = [
    path('', views.Home, name='Home'),
    path('login/', views.login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name='Home/logout.html'), name='logout'),
    path('about/', TemplateView.as_view(template_name='Home/about.html'), name='about'),
    path('register/', views.register, name='register'),
    path('contact/', TemplateView.as_view(template_name='Home/contact.html'), name='contact'),
    path('about/', TemplateView.as_view(template_name='Home/about.html'), name='about'),
]

urlpatterns += staticfiles_urlpatterns()
