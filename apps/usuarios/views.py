from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from apps.usuarios.helpers import CompararMatricula
from apps.usuarios.forms import LoginForms, CompararForms

def comparar(request):
    form = CompararForms()
    if request.method == 'POST':
        form = CompararForms(request.POST)
        if form.is_valid():
            usuario_com_lib=form['usuario_com_lib'].value()
            usuario_sem_lib=form['usuario_sem_lib'].value()
            usuario_efetua_liberacao=form['usuario_efetua_liberacao'].value()
            oracle, dbmaker, texto = CompararMatricula.comparacao(usuario_com_lib, usuario_sem_lib, usuario_efetua_liberacao)
        return render(request, 'usuarios/comparacao.html', {"form": form, 'oracle': oracle, 'dbmaker': dbmaker, 'texto': texto})
    return render(request, 'usuarios/comparacao.html', {"form": form})

def pesquisar(request):
    form = CompararForms()
    if request.method == 'POST':
        form = CompararForms(request.POST)
        if form.is_valid():
            usuario_com_lib=form['usuario_com_lib'].value()
            usuario_sem_lib=form['usuario_sem_lib'].value()
            oracle, dbmaker = CompararMatricula.pesquisarMatriculas(usuario_com_lib, usuario_sem_lib)
            return render(request, 'usuarios/comparacao.html', {"form": form, 'oracle': oracle, 'dbmaker': dbmaker})
    return render(request, 'usuarios/comparacao.html', {"form": form})

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
