from django.shortcuts import render, redirect
from .models import Area, Publico, Curso
from .forms import AreaForm, PublicoForm, CursoForm


# ===== FUNÇÃO - PÁGINA INICIAL ======

def home(request):
    return render(request, 'index.html')


# ===== FUNÇÕES - ÁREAS ======

def areas_listar(request):
    areas = Area.objects.all()
    contexto = {
        'lista_areas': areas
    }
    return render(request, 'areas.html', contexto)

def area_cadastro(request):
    form = AreaForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('areas_listar')
    contexto = {
        'form': form
    }
    return render(request, 'area_cadastro.html', contexto)

def area_editar(request, id):
    area = Area.objects.get(pk=id)
    
    form = AreaForm(request.POST or None, instance=area)
    if form.is_valid():
        form.save()
        return redirect('areas_listar')
    
    contexto = {
        'form': form
    }

    return render(request, 'area_cadastro.html', contexto)

def area_remover(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('areas_listar')



# ===== FUNÇÕES - PÚBLICOS ======

def publicos_listar(request):
    publicos = Publico.objects.all()
    contexto = {
        'lista_publicos': publicos
    }
    return render(request, 'publicos.html', contexto)

def publico_cadastro(request):
    form = PublicoForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('publicos_listar')
    contexto = {
        'form': form
    }
    return render(request, 'publico_cadastro.html', contexto)

def publico_editar(request, id):
    publico = Publico.objects.get(pk=id)
    
    form = PublicoForm(request.POST or None, instance=publico)
    if form.is_valid():
        form.save()
        return redirect('publicos_listar')
    
    contexto = {
        'form': form
    }

    return render(request, 'publico_cadastro.html', contexto)

def publico_remover(request, id):
    publico = Publico.objects.get(pk=id)
    publico.delete()
    return redirect('publicos_listar')



# ===== FUNÇÕES - CURSOS ======

def cursos_listar(request):
    cursos = Curso.objects.all()
    contexto = {
        'lista_cursos': cursos
    }
    return render(request, 'cursos.html', contexto)

def curso_cadastro(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('cursos_listar')
    contexto = {
        'form': form
    }
    return render(request, 'curso_cadastro.html', contexto)

def curso_editar(request, id):
    curso = Curso.objects.get(pk=id)
    
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('cursos_listar')
    
    contexto = {
        'form': form
    }

    return render(request, 'curso_cadastro.html', contexto)

def curso_remover(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('cursos_listar')
