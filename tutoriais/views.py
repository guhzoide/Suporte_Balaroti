from django.shortcuts import render, get_object_or_404
from tutoriais.models import cadastroTutoriais

def tutoriais(request):
    tutoriais = cadastroTutoriais.objects.order_by('titulo').filter(publicada=True)
    return render(request, 'tutoriais/tutoriais.html', {"tutoriais": tutoriais})


def visualizar(request, tutorial_id):
    texto = []
    tutorial = get_object_or_404(cadastroTutoriais, pk=tutorial_id)
    caminho_arquivo = tutorial.tutorial.path
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        texto = file.readlines()
    return render(request, 'tutoriais/visualizar.html', {"texto": texto})
