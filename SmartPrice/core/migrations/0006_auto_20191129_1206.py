# Generated by Django 2.2.7 on 2019-11-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191129_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='COD_BARR',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='Codigo de Barras'),
        ),
    ]