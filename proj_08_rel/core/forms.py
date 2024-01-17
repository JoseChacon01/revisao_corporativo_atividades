from django import forms
from .models import Area, Publico, Curso

class AreaForm(forms.ModelForm):
    class Meta:
           model = Area
           fields = ['nome']


class PublicoForm(forms.ModelForm):
    class Meta:
           model = Publico
           fields = ['nome']


class CursoForm(forms.ModelForm):
    class Meta:
           model = Curso
           fields = ['nome', 'data_inicio', 'vagas', 'area', 'publicos'] #pulou uma linha aqui. #Adicionado: 'area', 'publicos'
           widgets = { #alteração dos tipos de campos só é possivel utilizando o widgets
                'area': forms.RadioSelect(), #Utilizando o Radio no formulario django
                'publicos': forms.CheckboxSelectMultiple #Utilizando o checkbox no formulario django
           }