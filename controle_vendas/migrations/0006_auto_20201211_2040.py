# Generated by Django 3.1.4 on 2020-12-11 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_vendas', '0005_auto_20201211_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Ativo'), (2, 'Pendente'), (3, 'Concluido'), (4, 'Cancelado')], null=True, verbose_name='Status'),
        ),
    ]
