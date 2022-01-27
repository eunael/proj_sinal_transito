from itertools import chain
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Categorias'
    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(instance)
        for f in opts.many_to_many:
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data
    def __repr__(self):
        return str(self.to_dict())
    def __str__(self):
        return self.__repr__()
class Pergunta(models.Model):
    código = models.CharField(max_length=50, blank=True, null=True)
    enunciado = models.TextField(blank=True, null=False)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def getAlternativas(self):
        relAlternativas = self.objects.get(id=self.id).relperguntaalternativa
        alternativas = relAlternativas.alternativas
        return alternativas
    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(instance)
        for f in opts.many_to_many:
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data
    def __repr__(self):
        return str(self.to_dict())
    def __str__(self):
        return self.__repr__()
    class Meta:
        verbose_name_plural = 'Perguntas'

class Alternativa(models.Model):
    conteudo = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Alternativas'
    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(instance)
        for f in opts.many_to_many:
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data
    def __repr__(self):
        return str(self.to_dict())
    def __str__(self):
        return self.__repr__()

class RelPerguntaAlternativa(models.Model):
    id_pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    id_alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE)
    certa =  models.BooleanField(default=False)

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(instance)
        for f in opts.many_to_many:
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data
    def __repr__(self):
        return str(self.to_dict())
    def __str__(self):
        return self.__repr__()

# class RelAlternativaCategoria(models.Model):
#     id_alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE)
#     id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
#     certa =  models.BooleanField(default=False)