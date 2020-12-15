# Generated by Django 3.1.4 on 2020-12-11 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('controle_vendas', '0002_auto_20201211_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vendedor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Vendedor',
        ),
    ]
