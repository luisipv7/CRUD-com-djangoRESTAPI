from rest_framework import serializers
from app.models import Contato


class ContatoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contato
        fields = ('id',
                  'nome',
                  'idade',
                  'telefone',
                  'ativo')
