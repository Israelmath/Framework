# Generated by Django 3.2 on 2021-05-02 16:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0009_auto_20210425_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='dataCadastro',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 2, 13, 30, 4, 552854)),
        ),
    ]