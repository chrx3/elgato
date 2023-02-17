from rest_framework import serializers
from Gato.models import Gatito,Usuario
from rest_framework.authtoken.models import Token

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')

class GatitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gatito
        fields = ('__all__')