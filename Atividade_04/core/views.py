from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def cadastro (request, nome):
    contexto = {
        'nome': nome
    }
    return render(request, 'nome.html', contexto)


def idadeusu (request, suaidade):
    contexto = {
        'suaidade': suaidade,
        'suaidadee': 2022 - suaidade
    }
    return render(request, 'idade.html', contexto)
       


def mediaar (request, media1, media2): 
    contexto = {
        'media1': media1,
        'media2': media2,
        'mediafinal': (media1 + media2) / 2,
        
    }
    return render (request, 'media.html', contexto)   