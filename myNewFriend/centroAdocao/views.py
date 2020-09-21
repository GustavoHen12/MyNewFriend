from django.shortcuts import render
from django.http import HttpResponse
from .models import DadosCentroAdocao

def cadastroCentroAdocao(request):
    return render(request, 'cadastro.html')

def novoCentroAdocao(request):
    centro = DadosCentroAdocao()
    centro.nome = request.POST['nome']
    centro.email = request.POST['email']
    if(request.POST['cachorro'] == "on"):
        centro.cachorro = True
    else:
        centro.cachorro = False

    if(request.POST['gato'] == "on"):
        centro.gato = True
    else:
        centro.gato = False
        
    centro.quantidade = request.POST['quantidade']
    centro.save()
    return render(request, 'concluido.html')