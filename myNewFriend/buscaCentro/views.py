from django.shortcuts import render
from django.http import HttpResponse
from centroAdocao.models import DadosCentroAdocao

import logging

logger = logging.getLogger(__name__)

def resultadoBusca(request):
    lista = DadosCentroAdocao.objects.all()

    busca = request.GET.get("busca")
    if(busca):
        lista = DadosCentroAdocao.objects.filter(nome__contains = busca)

    logger.error(lista)
    return render(request, 'busca.html', {'Resultado': lista})