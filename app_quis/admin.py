from django.contrib import admin
from .models import Dificuldade, Pergunta, Alternativa, RelPerguntaAlternativa

admin.site.register(Dificuldade)
admin.site.register(Pergunta)
admin.site.register(Alternativa)
admin.site.register(RelPerguntaAlternativa)
