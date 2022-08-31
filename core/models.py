from pyexpat import model
from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=255)
    
class Editora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()
    