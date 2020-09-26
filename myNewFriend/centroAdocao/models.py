from django.db import models
class TestItem(models.Model):
    content = models.TextField()

# class testModel (models.Model):
#     nome: models.CharField(max_length=50)
#     email: models.EmailField(max_length=254)

# class centroAdocao (models.Model):
#     nome: models.CharField(max_length = 40)
#     email: models.EmailField(("email centro adocao"), max_length=254)
 
class DadosCentroAdocao (models.Model):
    nome = models.CharField(max_length = 40, default="invalido")
    email = models.EmailField(("email"), max_length=254, default="invalido")
    gato = models.BooleanField(default=False)
    quantidade = models.PositiveSmallIntegerField(default=0)
    img = models.ImageField(upload_to = "imagesData/", default="imagesData/erro.jpg") 

# MODEL CENTRO DE ADOÇÃO:
# nome
# email
# endereço
    #rua
    #numero
    #cep
    #estado
    #cidade
# Cachorro (boolean)
# Gato (boolean)
# foto
# quantos
# tempo post

#TODO: foto -> ImageField
#TODO: data -> DateField

#TODO: ver one to one relationship
#class endereco(models.Model):
#    rua: models.CharField