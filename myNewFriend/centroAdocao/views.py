from django.shortcuts import render
from django.http import HttpResponse
from .models import DadosCentroAdocao
from .forms import CadastroForm

import logging
logger = logging.getLogger(__name__)

def cadastroCentroAdocao(request):
    return render(request, 'cadastro.html')

def novoCentroAdocao(request):
    centro = DadosCentroAdocao()
    logger.error(request.POST)

    if request.method == "POST":
        form = CadastroForm(request.POST, request.FILES) 
        if form.is_valid():
            centro.img = request.FILES['image']
            centro.nome = request.POST['nome']
            centro.email = request.POST['email']
            centro.quantidade = request.POST['quantidade']

            if(request.POST['cachorro'] == None):
                centro.cachorro = False
            else:
                centro.cachorro = True

            if(request.POST['gato'] == None):
                centro.gato = False
            else:
                centro.gato = True
            # centro.save()
            return render(request, 'concluido.html')
        logger.error(form.errors)
    return render(request, 'cadastro.html')