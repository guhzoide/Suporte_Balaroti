from django.shortcuts import render, redirect
from django.contrib import messages
from apps.lojas.models import cadastroLojas, cadastroCameras, cadastroEtiquetas

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
    return render(request, 'lojas/ips.html', {"dados": cameras})

def ipEtiquetas(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    etiquetas = cadastroEtiquetas.objects.order_by("numero").filter(publicada=True)
    return render(request, 'lojas/ips.html', {"dados": etiquetas})