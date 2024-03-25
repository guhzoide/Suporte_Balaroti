from django.shortcuts import render, redirect
from django.contrib import messages
from cupom.helpers import Cupom
from cupom.forms import formsCupom

def cupom(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    form = formsCupom()
    msg=""
    dados=[]
    quantidade='0'
    if request.method == 'POST':
        form = formsCupom(request.POST)
        
        if form.is_valid():
            data=str(form['data'].value())
            numero_cupom=str(form['numero_cupom'].value())

            msg, dados, quantidade = Cupom.consultaCupom(data, numero_cupom)
    
            return render(request, 'cupom/cupom.html', {"msg":msg, "dados":dados, "quantidade":quantidade, "form": form})
        else:
            msg="Ocorreu um erro ao iniciar a tela"
            return render(request, 'cupom/cupom.html', {"msg":msg, "dados":dados, "quantidade":quantidade, "form": form})
    return render(request, 'cupom/cupom.html', {"msg":msg, "dados":dados, "quantidade":quantidade, "form": form})

def consultaMovimento(request):
    form = formsCupom()
    msg, dados, quantidade = Cupom.situacaoAtual()
    return render(request, 'cupom/cupom.html', {"msg":msg, "dados":dados, "quantidade":quantidade, "form": form})