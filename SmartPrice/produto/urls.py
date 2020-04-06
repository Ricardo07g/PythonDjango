from django.conf.urls import url
from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'produto'
urlpatterns = [
    path('listar/', views.ListaProdutos, name='listaProdutos'),
    path('cadastro/', views.CadProduto, name='CadProduto'),
    path('editar/<COD_BARR>/', views.EditaProduto, name='editaProduto'),
    path('deletar/<COD_BARR>/', views.DeletaProduto, name='deletaProduto'),
]
