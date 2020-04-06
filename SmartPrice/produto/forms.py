from django import forms
from SmartPrice.core.models import produto
from django.db import models
from django.forms import ModelForm


class ContactProduto(forms.Form):
    COD_BARR = forms.CharField(label='CÓDIGO DE BARRA', widget=forms.TextInput(attrs={'size': 48}), max_length=15)
    UM = forms.CharField(label='UNIDADE DE MEDIDA', widget=forms.TextInput(attrs={'size': 48}), max_length=3)
    TAGS = forms.CharField(label='TAGS', widget=forms.TextInput(attrs={'size': 48}), max_length=240)
    EMBALAGEM = forms.CharField(label='QUANTIDADE', widget=forms.TextInput(attrs={'size': 48}), max_length=10)
    DESCRIC = forms.CharField(label='DESCRIÇÃO', widget=forms.Textarea)


class ProductForm(forms.ModelForm):
    COD_BARR = forms.CharField(label='CÓDIGO DE BARRA', widget=forms.TextInput(attrs={'size': 48}), max_length=15)
    UM = forms.CharField(label='UNIDADE DE MEDIDA', widget=forms.TextInput(attrs={'size': 48}), max_length=3)
    TAGS = forms.CharField(label='TAGS', widget=forms.TextInput(attrs={'size': 48}), max_length=240)
    EMBALAGEM = forms.CharField(label='QUANTIDADE', widget=forms.TextInput(attrs={'size': 48}), max_length=10)
    DESCRIC = forms.CharField(label='DESCRIÇÃO', widget=forms.Textarea)

    class Meta:
        model = produto
        fields = ['COD_BARR', 'UM', 'TAGS', 'EMBALAGEM', 'DESCRIC']


class EditProduto(forms.ModelForm):
    COD_BARR = forms.CharField(label='CÓDIGO DE BARRA', widget=forms.TextInput(attrs={'size': 48}), max_length=15, disabled=True)
    UM = forms.CharField(label='UNIDADE DE MEDIDA', widget=forms.TextInput(attrs={'size': 48}), max_length=3)
    TAGS = forms.CharField(label='TAGS', widget=forms.TextInput(attrs={'size': 48}), max_length=240)
    EMBALAGEM = forms.CharField(label='QUANTIDADE', widget=forms.TextInput(attrs={'size': 48}), max_length=10)
    DESCRIC = forms.CharField(label='DESCRIÇÃO', widget=forms.Textarea)

    class Meta:
        model = produto
        fields = ('COD_BARR', 'UM', 'TAGS', 'EMBALAGEM', 'DESCRIC')
