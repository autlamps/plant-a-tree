from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

from store.models import Product


@require_http_methods(["GET"])
def get_product(request, item_id):
    item = get_object_or_404(Product, pk=item_id)
    return render(request, 'product.html', context={
        'product': item,
    })