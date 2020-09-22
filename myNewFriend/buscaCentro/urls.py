from django.urls import path
from . import views

urlpatterns = [
    path('', views.resultadoBusca, name='resultadoBusca'),
]