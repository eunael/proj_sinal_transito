from random import shuffle
from django.shortcuts import redirect, render
from django.http import HttpResponse

from app_quis.models import Alternativa, Pergunta, RelPerguntaAlternativa

def view_obj(obj):
    strObj = ""
    for i in obj:
        strObj += str(i).replace(", '", ", <br>'")
        strObj += "<br><br>"
    # return str(obj).replace('}, {', '}, <br>{')
    return strObj

def index(request):
    data = {}
    list_perg = list()
    perguntas = Pergunta.objects.all()
    perguntas_ids = list(map(lambda x: x.id, perguntas))
    shuffle(perguntas_ids)
    perguntas_ids = perguntas_ids[0:10]
    count = 1
    for idx, id_p in enumerate(perguntas_ids):
        perg = perguntas.get(pk=id_p)
        alterns_ids = list(RelPerguntaAlternativa.objects.filter(id_pergunta=perg.id).values_list('id_alternativa', flat=True))
        alterns = list(Alternativa.objects.filter(id__in=alterns_ids))
        if len(alterns_ids)>0:
            obj = {
                'pergunta': perg,
                'alternativas': alterns,
                'index': count
            }
            list_perg.append(obj)
            count += 1
    data['questoes'] = list_perg
    
    # return HttpResponse(view_obj(list_perg))

    return render(request, 'app_quis/index.html', data)

def enviaSimulado(request):
    if request.method == 'POST':
        '''if request.POST.get('name') != "" and request.POST.get('email') != "" and request.POST.get('subject') != "" and request.POST.get('message') != "":
            blog = Blog.objects.filter(id=request.POST.get('id_blog')).first()
            contact = Contact()
            contact.blog_id = blog
            contact.name = request.POST.get('name')
            contact.email = request.POST.get('email')
            contact.subject = request.POST.get('subject')
            contact.message = request.POST.get('message')
            contact.save()

            return redirect('blog_index')
        return HttpResponse("Você não preencheu algum campo 🤔")'''
        list_keys = list(request.POST.dict().keys())
        list_vals = list(request.POST.dict().values())
        qst_resp = []

        for i, key in enumerate(list_keys):
            if('perg' in key):
                qst_resp.append({'id_pegunta': str(list_vals[i])})
            elif('resp' in key):
                qst_resp[int(key[-1])-1]['id_alternativa'] = list_vals[i]

        return HttpResponse(qst_resp)
    return HttpResponse("Não é métofo post.")
