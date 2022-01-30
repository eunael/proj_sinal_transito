from django.db import models

class Placa(models.Model):
    imagem = models.ImageField(upload_to='placas/', default=None)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
