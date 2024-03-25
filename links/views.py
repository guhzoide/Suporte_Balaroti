from django.shortcuts import render, redirect
from django.contrib import messages
from links.models import cadastroLinks

def links(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    links = cadastroLinks.objects.order_by('nome').filter(publicada=True)
    return render(request, 'links/links.html', {"links": links})
