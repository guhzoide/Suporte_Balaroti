from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.tutoriais.models import cadastroTutoriais

def tutoriais(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    tutoriais = cadastroTutoriais.objects.order_by('titulo').filter(publicada=True)
    return render(request, 'tutoriais/tutoriais.html', {"tutoriais": tutoriais})


def visualizar(request, tutorial_id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    texto = []
    tutorial = get_object_or_404(cadastroTutoriais, pk=tutorial_id)
    caminho_arquivo = tutorial.tutorial.path
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        texto = file.readlines()
    return render(request, 'tutoriais/visualizar.html', {"texto": texto})
