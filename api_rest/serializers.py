from rest_framework import serializers

from .models import Endereco, Loja, Plataforma, Vendedor

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = '__all__'

class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = '__all__'

class VendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'