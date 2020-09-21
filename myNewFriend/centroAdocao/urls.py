from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastroCentroAdocao, name='cadastroCentroAdocao'),
    path('novoCentroAdocao/', views.novoCentroAdocao, name='novoCentroAdocao'),
]