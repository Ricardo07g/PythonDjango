# Generated by Django 2.2.7 on 2019-11-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_produto_cod_barr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='id',
        ),
        migrations.AlterField(
            model_name='produto',
            name='COD_BARR',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Codigo de Barras'),
        ),
    ]
