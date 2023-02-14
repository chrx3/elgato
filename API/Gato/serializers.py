from rest_framework import serializers
from Gato.models import Gatito,Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('Id', 'Username', 'Password')

class GatitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gatito
        fields = ('id','Gato')