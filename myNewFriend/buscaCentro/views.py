from django.shortcuts import render
from django.http import HttpResponse
from centroAdocao.models import DadosCentroAdocao
from buscaCentro.mapEstados import mapEstadosSigla

import logging

logger = logging.getLogger(__name__)

def resultadoBusca(request):
    lista = DadosCentroAdocao.objects.all()

    nomeEstado = request.GET.get("estado")
    cidade = request.GET.get("cidade")

    estado = mapEstadosSigla(nomeEstado)
    if(estado):
        lista = DadosCentroAdocao.objects.filter(endereco__estado__iexact = estado, endereco__cidade__contains = cidade)

    logger.error(lista)
    return render(request, 'busca.html', {'Resultado': lista, 'cidade': cidade, 'estado': estado, 'total': len(lista)})

    
