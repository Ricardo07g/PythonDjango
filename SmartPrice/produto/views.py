from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.urls import reverse_lazy

from SmartPrice.core.models import produto
from SmartPrice.produto.forms import ContactProduto, EditProduto
from django.contrib.auth.decorators import login_required
from django.template import loader


# Create your views here.
@login_required(login_url='accounts:login')
def ListaProdutos(request):
    lista = produto.objects.all()
    template = 'produto/ListaProduto.html'
    context = {}
    if request.method == 'POST':
        form = ContactProduto(request.POST)
        if form.is_valid():
            produto_form = produto.objects.get_or_create()(
                COD_BARR=form.cleaned_data['COD_BARR'],
                UM=form.cleaned_data['UM'],
                TAGS=form.cleaned_data['TAGS'],
                EMBALAGEM=form.cleaned_data['EMBALAGEM'],
                DESCRIC=form.cleaned_data['DESCRIC'])
            produto_form.Save()
            context['is_valid'] = True
            form = ContactProduto()
    else:
        form = ContactProduto()

    context['formulario'] = form
    context['lista_produtos'] = lista
    return render(request, template, context)


@login_required(login_url='accounts:login')
def CadProduto(request):
    template = 'produto/cadProduto.html'
    context = {}
    form = ContactProduto()
    context['formulario'] = form
    if request.method == 'POST':
        form = ContactProduto(request.POST)
        if form.is_valid():
            prod = produto.objects.get_or_create(
                COD_BARR=form.cleaned_data['COD_BARR'],
                UM=form.cleaned_data['UM'],
                TAGS=form.cleaned_data['TAGS'],
                EMBALAGEM=form.cleaned_data['EMBALAGEM'],
                DESCRIC=form.cleaned_data['DESCRIC'])
            context['is_valid'] = True
            return render(request, template, context)
    else:
        return render(request, template, context)


@login_required(login_url='accounts:login')
def EditaProduto(request, COD_BARR):
    template = 'produto/EditaProduto.html'
    context = {}
    form = EditProduto()
    context['formulario'] = form
    if request.method == "POST":
        post = get_object_or_404(produto, COD_BARR=COD_BARR)
        form = EditProduto(request.POST, instance=post)
        if form.is_valid():
            # post = form.save(commit=False)
            post.COD_BARR = form.cleaned_data['COD_BARR']
            post.UM = form.cleaned_data['UM']
            post.TAGS = form.cleaned_data['TAGS']
            post.EMBALAGEM = form.cleaned_data['EMBALAGEM']
            post.DESCRIC = form.cleaned_data['DESCRIC']
            post.save()
            lista = produto.objects.all()
            template = 'produto/ListaProduto.html'
            context['lista_produtos'] = lista
            # return render(request, 'produto/ListaProduto.html', context)
            # render(request, template, context)
            return render(request, template, context)
        else:
            return print("NOT VALID")
    else:
        post = get_object_or_404(produto, COD_BARR=COD_BARR)
        form = EditProduto(instance=post)
        context['formulario'] = form
        return render(request, template, context)


@login_required(login_url='accounts:login')
def DeletaProduto(request, COD_BARR):
    Item = produto.objects.get(COD_BARR=COD_BARR)
    Item.delete()

    context = {}
    lista = produto.objects.all()
    template = 'produto/ListaProduto.html'
    context['lista_produtos'] = lista

    return render(request, template, context)