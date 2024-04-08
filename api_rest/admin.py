from django.contrib import admin

# Register your models here.
from .models import Endereco, Plataforma, Loja, Vendedor

admin.site.register(Endereco)
admin.site.register(Plataforma)
admin.site.register(Loja)
admin.site.register(Vendedor)