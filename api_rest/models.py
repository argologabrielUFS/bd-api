from django.db import models

# Create your models here.
class Endereco(models.Model):
    
    cpf = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=150, default='')
    cidade = models.CharField(max_length=150, default='')
    logradouro = models.CharField(max_length=150, default=0)

class Plataforma(models.Model):
    
    cnpj = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150, default='')

class Vendedor(models.Model):
    
    id_vend = models.IntegerField(primary_key=True)
    vendas = models.IntegerField(default='')

class Loja(models.Model):
    
    cnpj = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150, default='')
    email = models.EmailField(max_length=150, default='')
    fk_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, null=True, blank=True)
    