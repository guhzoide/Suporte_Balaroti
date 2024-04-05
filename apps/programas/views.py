from django.shortcuts import render, redirect
from django.contrib import messages
from apps.programas.helpers import helpersProgramas
from apps.programas.models import status

def programas(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    valor = status.objects.filter(status_atual=True)
    if valor:
        messages.error(request, "Atenção!! Já existe um processo em execução.")
        return render(request, 'programas/programas.html')
    

    return render(request, 'programas/programas.html')

def verificaProgramas(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')

    valor = status.objects.filter(status_atual=True)
    if valor == True:
        return redirect('programas')

    status.objects.update(status_atual=True)
    dados = helpersProgramas.verificaprog()
    status.objects.update(status_atual=False)
    return render(request, 'programas/programas.html', {"dados":dados})

def desativatudo(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')

    valor = status.objects.filter(status_atual=True)
    if valor == True:
        return redirect('programas')

    status.objects.update(status_atual=True)
    dados = helpersProgramas.desativatudo()
    status.objects.update(status_atual=False)
    return render(request, 'programas/programas.html', {"dados":dados})