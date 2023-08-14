from django.db import models

# Create your models here.

class Comanda(models.Model):
    numero = models.CharField(max_length=5)

    def __str__(self):
        return f"Comanda {self.numero}"

class Pedido(models.Model):
    data_pedido = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)

class Prato(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome