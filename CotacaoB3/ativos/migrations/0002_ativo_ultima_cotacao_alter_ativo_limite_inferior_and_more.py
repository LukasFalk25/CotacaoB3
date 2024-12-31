# Generated by Django 5.1.4 on 2024-12-27 15:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ativos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ativo',
            name='ultima_cotacao',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ativo',
            name='limite_inferior',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='ativo',
            name='limite_superior',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]