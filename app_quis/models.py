from django.db import models


class Dificuldade(models.Model):
    nome = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Dificuldades'
    def __str__(self):
        return self.nome
class Pergunta(models.Model):
    código = models.CharField(max_length=50, null=True)
    enunciado = models.TextField(null=False)
    id_dificuldade = models.ForeignKey(Dificuldade, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Perguntas'
    def __str__(self):
        return self.enunciado

class Alternativa(models.Model):
    conteudo = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Alternativas'
    def __str__(self):
        return self.conteudo

class RelPerguntaAlternativa(models.Model):
    id_pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    id_alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE)
    certa =  models.BooleanField(default=False)
