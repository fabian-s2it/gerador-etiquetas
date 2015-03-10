from rest_framework import serializers
from models import Etiqueta, ModoLavagem, Composicao


class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = ('id', 'artigo', 'unidade', 'largura')

class ModoLavagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModoLavagem
        fields = ('id', 'descricao', 'imagem', 'etiqueta')

class ComposicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composicao
        fields = ('id', 'descricao', 'etiqueta')