from django.db import models

class Area(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self): #def __str__ ----> O __str__: Para retornar um valor padrão ao acessar um objeto, é necessário criar uma função chamada __str__, e retornar o atributo que desejar do Model.
        return self.nome 

class Publico(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self): #def __str__
        return self.nome 

class Curso(models.Model):
    nome = models.CharField('Nome', max_length=100)
    data_inicio = models.DateField('Data de Início')
    vagas = models.IntegerField('Vagas')
    area = models.ForeignKey(Area, on_delete=models.PROTECT) #Rel. muitos para 1, entre cursos e area // #Adicionado: on_delete=models.CASCADE #Mudar, CASCADE para PROTECT -- NO PROTECT EXIBE UMA MENSAGEM DE PROTEÇÃO/ ALERTA, CASO O USUARIO QUEIRA ALTERAR ALGO SEM A PERMIÇÃO DO ADMINISTRADOR
    publicos = models.ManyToManyField(Publico) #gerando a tabela intermediária automaticamente.

