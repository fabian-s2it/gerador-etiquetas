from django.db import models

class Etiqueta(models.Model):

    id = models.AutoField(primary_key=True)
    artigo = models.CharField(max_length=250)
    unidade = models.CharField(max_length=40)
    largura = models.CharField(max_length=40)

    def __unicode__(self):
        return self.artigo

class Composicao(models.Model):

    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=200)
    etiqueta = models.ForeignKey(Etiqueta, null=False)

    def __unicode__(self):
        return self.descricao

class ModoLavagem(models.Model):

    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=200)
    imagem = models.CharField(max_length=250)
    etiqueta = models.ForeignKey(Etiqueta, null=True)

    def __unicode__(self):
        return self.descricao
