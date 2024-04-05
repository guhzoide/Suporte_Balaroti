from django.shortcuts import render, redirect
from django.contrib import messages
from apps.cupom.helpers import Cupom
from apps.cupom.forms import formsCupom

def cupom(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    form = formsCupom()
    dados=[]
    quantidade='0'
    if request.method == 'POST':
        form = formsCupom(request.POST)
        
        if form.is_valid():
            data=str(form['data'].value())
            numero_cupom=str(form['numero_cupom'].value())

            msg, dados, quantidade = Cupom.consultaCupom(data, numero_cupom)
            messages.error(request, msg)
    
            return render(request, 'cupom/cupom.html', {"dados":dados, "quantidade":quantidade, "form": form})
        else:
            msg="Ocorreu um erro ao iniciar a tela"
            messages.error(request, msg)
            return render(request, 'cupom/cupom.html', {"dados":dados, "quantidade":quantidade, "form": form})
    return render(request, 'cupom/cupom.html', {"dados":dados, "quantidade":quantidade, "form": form})

def consultaMovimento(request):
    form = formsCupom()
    msg, dados, quantidade = Cupom.situacaoAtual()
    messages.error(request, msg)
    return render(request, 'cupom/cupom.html', {"dados":dados, "quantidade":quantidade, "form": form})