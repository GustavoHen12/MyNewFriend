from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.post_list, name='cadastroCentroAdocao'),
]