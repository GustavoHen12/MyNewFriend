from django.db import models
class Endereco(models.Model):
    rua = models.CharField(max_length=200, null=False, blank=False)
    cep = models.IntegerField(null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.rua

class DadosCentroAdocao (models.Model):
    nome = models.CharField(max_length = 40, default="invalido")
    email = models.EmailField(("email"), max_length=254, default="invalido")
    gato = models.BooleanField(default=False)
    cachorro = models.BooleanField(default=False)
    quantidade = models.PositiveSmallIntegerField(default=0)
    img = models.ImageField(upload_to = "imagesData/", default="imagesData/erro.jpg")
    endereco = models.OneToOneField(Endereco, models.CASCADE, null=True) 