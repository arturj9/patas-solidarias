from django.db import models
from django.contrib.auth.models import User

class Raca(models.Model):
    raca = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return str(self.raca)
    
        
class Tag(models.Model):
    tag = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return str(self.tag)

class Pet(models.Model):
    choices_status = (('P', 'Para adoção'), 
                      ('A', 'Adotado'))
    
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos_pets')
    descricao = models.TextField()
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=14)
    status = models.CharField(max_length=1, choices=choices_status)
    
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    raca = models.ForeignKey(Raca, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self) -> str:
        return str(self.nome)