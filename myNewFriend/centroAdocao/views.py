from django.shortcuts import render
from django.http import HttpResponse
from .models import DadosCentroAdocao, Endereco
from .forms import CadastroForm

import logging
logger = logging.getLogger(__name__)

def cadastroCentroAdocao(request):
    return render(request, 'cadastro.html')

def novoCentroAdocao(request):
    centro = DadosCentroAdocao()
    endereco = Endereco()
    logger.error(request.POST)

    if request.method == "POST":
        form = CadastroForm(request.POST, request.FILES) 
        if form.is_valid():
            centro.img = request.FILES['image']
            centro.nome = request.POST['nome']
            centro.email = request.POST['email']
            centro.quantidade = request.POST['quantidade']

            if(request.POST['cachorro'] == "0"):
                centro.cachorro = False
            else:
                centro.cachorro = True

            if(request.POST['gato'] == "0"):
                centro.gato = False
            else:
                centro.gato = True

            endereco.rua = request.POST['rua']
            endereco.cep = request.POST['cep']
            endereco.cidade = request.POST['cidade']
            endereco.estado = request.POST['estado']
            endereco.bairro = request.POST['bairro']
            endereco.numero = request.POST['numero']
            endereco.save()

            centro.endereco = endereco
            centro.save()
            return render(request, 'concluido.html')
        logger.error(form.errors)
    return render(request, 'cadastro.html')