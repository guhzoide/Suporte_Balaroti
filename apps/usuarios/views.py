from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            return redirect('index')
        else:
            messages.error(request, "Usuário ou senha incorretos!")
            return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})

def logout(request):
    auth.logout(request)
    return redirect('login')
