from django.db import models
from django.contrib.auth.models import User


class Grupo(models.Model):
    nome = models.CharField(max_length=100)
   
    def __str__(self):
        return self.nome

#
class Participante(models.Model):
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='participantes')

    def __str__(self):
        return f"{self.usuario.username} no grupo '{self.grupo.nome}'"