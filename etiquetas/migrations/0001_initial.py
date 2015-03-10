# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Composicao',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('artigo', models.CharField(max_length=250)),
                ('unidade', models.CharField(max_length=40)),
                ('largura', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModoLavagem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=200)),
                ('imagem', models.CharField(max_length=250)),
                ('etiqueta', models.ForeignKey(to='etiquetas.Etiqueta', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='composicao',
            name='etiqueta',
            field=models.ForeignKey(to='etiquetas.Etiqueta'),
            preserve_default=True,
        ),
    ]
