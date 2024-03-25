from django.shortcuts import render, redirect
from django.contrib import messages
from lojas.models import cadastroLojas, cadastroCameras

def lojas(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    return render(request, 'lojas/lojas.html')

def listaLojas(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    lojas = cadastroLojas.objects.order_by("numero").filter(publicada=True)
    return render(request, 'lojas/lista_lojas.html', {"lojas": lojas})

def ipCameras(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    cameras = cadastroCameras.objects.order_by("numero").filter(publicada=True)
    return render(request, 'lojas/ipcameras.html', {"cameras": cameras})