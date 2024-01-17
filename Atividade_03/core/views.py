from django.shortcuts import render

# Create your views here.
def index (request):
    return render (request, 'index.html')

def pagina2 (request):
    return render (request, 'pagina_2.html')    

def pagina3 (request):
    return render (request, 'pagina_3.html')        