from django.shortcuts import render

# Create your views here.
def nome_aluno(request):
    return render(request, 'nome.html')

def index (request):
    return render (request, 'index.html')

def campus (request):
    return render (request, 'campus.html')

