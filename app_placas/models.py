from itertools import chain
from django.db import models

class Placa(models.Model):
    imagem = models.TextField(blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=250, blank=True, null=True)

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
