# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionDesRestos', '0005_auto_20170630_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restos2',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionDesRestos.Categorie'),
        ),
    ]
