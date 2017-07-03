# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionDesRestos', '0002_auto_20170629_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restos2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=42)),
                ('contenu', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionDesRestos.Restos2')),
            ],
        ),
    ]