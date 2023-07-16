from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from . import forms

# Create your views here.


@login_required
def home(request):
    return render(request, 'Home/index.html')


def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                return redirect(request, 'home/index.html', {"mensaje": "Inicio de sesión exitoso"})
    else:
        form = forms.CustomAuthenticationForm()
    return render(request, 'Home/login.html', {'form': forms})
