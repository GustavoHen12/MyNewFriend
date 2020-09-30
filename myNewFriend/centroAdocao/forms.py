from django.forms import ModelForm 
from django import forms 
from .models import * 
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

import logging
logger = logging.getLogger(__name__)

class CadastroForm(ModelForm): 
    class Meta: 
        model = DadosCentroAdocao         
        fields =["nome", "email", "quantidade", "img"] 
  
    def clean(self): 
        super(CadastroForm, self).clean() 

        email = self.cleaned_data.get('email')  
        nome = self.cleaned_data.get('nome') 
        quantidade = self.cleaned_data.get('quantidade')  
        img = self.files.get('image')  
    
        if len(nome) < 5: 
            self._errors['nome'] = self.error_class([ 
                'Minimo de 5 caracteres'])
        if email == None: 
            self._errors['email'] = self.error_class([ 
                'Email invalido'])
        if quantidade <= 0 or quantidade == None: 
            self._errors['qunatidade'] = self.error_class([ 
                'Quantidade inválida'])
        if img == None: 
            self._errors['image'] = self.error_class([ 
                'Adicione uma imagem'])
        return self.cleaned_data 
  