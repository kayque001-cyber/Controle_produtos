from django.shortcuts import render
from .models import Product, Brand, Category


def index(request):

    produtos = Product.objects.all()
    quantidade_produtos = Product.objects.count()
    quantidade_categorias = Category.objects.count()
    quantidade_marcas = Brand.objects.count()

    contexto = {
        'produtos': produtos,
        'quantidade_produtos': quantidade_produtos,
        'quantidade_categorias': quantidade_categorias,
        'quantidade_marcas': quantidade_marcas,
    }

    return render(request, 'pages/index.html', contexto)
