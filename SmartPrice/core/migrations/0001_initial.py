# Generated by Django 2.2.7 on 2019-11-26 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COD_BARR', models.CharField(max_length=15)),
                ('UM', models.CharField(max_length=3)),
                ('TAGS', models.CharField(max_length=240)),
                ('EMBALAGEM', models.CharField(max_length=10)),
                ('DESCRIC', models.TextField()),
            ],
        ),
    ]
