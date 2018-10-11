from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from store.models import Tree, Product


@require_http_methods(["GET"])
def show_all(request):
    trees = set()
    products = set()

    trees.update(Tree.objects.all())
    products.update(Product.objects.all())

    return render(request, 'all.html', context={
        'trees': trees,
        'products': products,
        'page_title': "All"
    })


def show_trees(request):
    trees = set()

    trees.update(Tree.objects.all())

    return render(request, 'all.html', context={
        'trees': trees,
        'page_title': "All Trees"
    })


def show_products(request):
    products = set()

    products.update(Product.objects.all())

    return render(request, 'all.html', context={
        'products': products,
        'page_title': "All Products"
    })
