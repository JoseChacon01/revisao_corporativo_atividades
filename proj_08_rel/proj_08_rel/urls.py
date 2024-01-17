"""proj_08_rel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home
from core.views import areas_listar, area_cadastro, area_editar, area_remover
from core.views import publicos_listar, publico_cadastro, publico_editar, publico_remover
from core.views import cursos_listar, curso_cadastro, curso_editar, curso_remover


urlpatterns = [
    # Rota para Página Inicial
    path('', home, name='home'),

    # Rotas para Área
    path('areas/', areas_listar, name='areas_listar'),
    path('area_cadastro/', area_cadastro, name='area_cadastro'),
    path('area_editar/<int:id>/', area_editar, name='area_editar'),
    path('area_remover/<int:id>/', area_remover, name='area_remover'),

    # Rotas para Público
    path('publicos/', publicos_listar, name='publicos_listar'),
    path('publico_cadastro/', publico_cadastro, name='publico_cadastro'),
    path('publico_editar/<int:id>/', publico_editar, name='publico_editar'),
    path('publico_remover/<int:id>/', publico_remover, name='publico_remover'),

    # Rotas para Curso
    path('cursos/', cursos_listar, name='cursos_listar'),
    path('curso_cadastro/', curso_cadastro, name='curso_cadastro'),
    path('curso_editar/<int:id>/', curso_editar, name='curso_editar'),
    path('curso_remover/<int:id>/', curso_remover, name='curso_remover'),

    path('admin/', admin.site.urls),
]
