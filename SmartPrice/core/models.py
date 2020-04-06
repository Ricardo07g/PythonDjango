from django.db import models


# Create your models here.
class produtoManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(COD_BAR__iconstais=query)


class produto(models.Model):
    COD_BARR = models.CharField('Codigo de Barras', max_length=15, primary_key=True, unique=True)
    UM = models.CharField('Unidade de Medida', max_length=3)
    TAGS = models.CharField('Tags', max_length=240)
    EMBALAGEM = models.CharField('Embalagem', max_length=10)
    DESCRIC = models.TextField('Descrição')
    objects = produtoManager()

    def __str__(self):
        return self.COD_BARR

    def __unicode__(self):
        return self.COD_BARR

