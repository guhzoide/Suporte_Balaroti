from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from apps.usuarios.helpers import LiberarMatricula
from apps.usuarios.forms import LoginForms, CompararForms, LiberarForms, ContaOmniForms
from apps.usuarios.models import cadastroCodigoOmni

def liberacoes(request):
    return render(request, "usuarios/liberacoes.html")

def comparar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    form = CompararForms()
    if request.method == 'POST':
        form = CompararForms(request.POST)
        if form.is_valid():
            usuario_com_lib=form['usuario_com_lib'].value()
            usuario_sem_lib=form['usuario_sem_lib'].value()
            usuario_efetua_liberacao=form['usuario_efetua_liberacao'].value()
            perfis, dbmaker, texto = LiberarMatricula.comparacao(usuario_com_lib, usuario_sem_lib, usuario_efetua_liberacao)
        return render(request, 'usuarios/comparacao.html', {"form": form, 'perfis': perfis, 'dbmaker': dbmaker, 'texto': texto})
    return render(request, 'usuarios/comparacao.html', {"form": form})

def liberarVendas(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    form = LiberarForms()
    if request.method == 'POST':
        form = LiberarForms(request.POST)
        if form.is_valid():
            usuario_lib=form['usuario_lib'].value()
            usuario_efetua_liberacao=form['usuario_efetua_liberacao'].value()
            texto = LiberarMatricula.liberar(usuario_lib, usuario_efetua_liberacao)
            return render(request, 'usuarios/liberacao_vendas.html', {"form": form, 'texto': texto})
    return render(request, 'usuarios/liberacao_vendas.html', {"form": form})

def contaOmni(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    texto = ''

    form = ContaOmniForms()
    if request.method == 'POST':
        form = ContaOmniForms(request.POST)
        if form.is_valid():
            acesso=form['acesso'].value()
            loja=form['loja'].value()
            nome=form['nome'].value()
            email=form['email'].value()
            matricula=form['matricula'].value()
            senha = f"Bala@{matricula}"
            email = email.strip()

            texto = LiberarMatricula.criarEmailZimbra(email, senha, acesso, nome)
            if acesso == 'Gestao':
                dados = cadastroCodigoOmni.objects.filter(numero=loja, acesso='GESTAO')
                for line in dados:
                    descricao_gestao = line.descricao
                    codigo_gestao = line.codigo
                
                dados = cadastroCodigoOmni.objects.filter(numero=loja, acesso='VENDEDOR')
                for line in dados:
                    descricao_vendedor = line.descricao
                    codigo_vendedor = line.codigo
                texto = LiberarMatricula.gerenteContaOmni(nome, email, matricula, senha, descricao_vendedor, codigo_vendedor, descricao_gestao, codigo_gestao)

            else:
                dados = cadastroCodigoOmni.objects.filter(numero=loja, acesso='VENDEDOR')
                for line in dados:
                    print(line)
                    descricao_vendedor = line.descricao
                    codigo_vendedor = line.codigo 
                texto = LiberarMatricula.vendedorContaOmni(nome, email, matricula, senha, descricao_vendedor, codigo_vendedor)
        return render(request, 'usuarios/contaOmni.html', {"form": form, "texto": texto})
    return render(request, 'usuarios/contaOmni.html', {"form": form})

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome=form['nome_login'].value()
            nome = nome.lower()
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
