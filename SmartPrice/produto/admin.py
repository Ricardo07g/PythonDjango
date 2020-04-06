from django.contrib import admin
from SmartPrice.core.models import produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['COD_BAR', 'UM', 'TAGS', 'EMBALAGEM', 'DESCRIC']
    search_fields = ['COD_BAR']


admin.site.register(produto)
