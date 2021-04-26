# Generated by Django 3.2 on 2021-04-26 01:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receitas', '0008_alter_receita_datacadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='receita',
            name='dataCadastro',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 25, 22, 9, 47, 698553)),
        ),
    ]
