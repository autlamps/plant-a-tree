from django.shortcuts import get_list_or_404, render
from django.views.decorators.http import require_http_methods

from store.models import Tree, Product


@require_http_methods(["GET"])
def get_item(request):
    queries = request.GET.get("words")
    trees = set()
    products = set()
    if queries is not None:
        queries = queries.split()
        for query in queries:
            trees.update(Tree.objects.filter(name__icontains=query))
            trees.update(Tree.objects.filter(description__icontains=query))

            products.update(Product.objects.filter(name__icontains=query))
            products.update(Product.objects.filter(
                description__icontains=query))

    return render(request, 'search.html', context={
        'trees': trees,
        'products': products,
        'page_title': "Search"
    })
