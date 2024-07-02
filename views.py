from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')
    
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                correo=cd['correo'],  # Asegúrate de que los campos coincidan con tu formulario
                                password=cd['password'],
                                )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Usuario creado exitosamente')
                else:
                    return HttpResponse('Usuario no creado.')
            else:
                return HttpResponse('Usuario inválido')
        else:
            # Corregido: form = LoginForm -> form = LoginForm()
            form = LoginForm()
            return render(request, 'task/login.html', {'form': form})
    else:
        form = LoginForm()  # Asegúrate de crear el formulario incluso si no es un POST
        return render(request, 'task/login.html', {'form': form})

        
        
