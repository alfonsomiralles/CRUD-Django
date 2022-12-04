from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado con éxito')
            return redirect('index')
        else:
            messages.error(request, 'El Usuario no ha podido ser creado')
            return redirect('register')
    else:
        form = UserCreationForm
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
