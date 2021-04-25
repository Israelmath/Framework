# Generated by Django 3.2 on 2021-04-25 19:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('receitas', '0003_alter_receita_datacadastro'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='autor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receita',
            name='dataCadastro',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 25, 16, 13, 55, 606556)),
        ),
    ]
