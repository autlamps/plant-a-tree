from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from random import randint
from store.models import Tree
from store.models import Product


@require_http_methods(["GET"])
def index_view(request):
    item1 = Product.objects.get(pk=randint(1, Product.objects.count()))
    item2 = Product.objects.get(pk=randint(1, Product.objects.count()))
    item3 = Tree.objects.get(pk=randint(1, Tree.objects.count()))
    item4 = Tree.objects.get(pk=randint(1, Tree.objects.count()))

    return render(request, 'index.html', context={'location1': item1,
                                                  'location2': item2,
                                                  'location3': item3,
                                                  'location4': item4})

# checks the prodcuts in database
# displays in front page
# selected 10 products and randomly puts them to screen
# random generater to choose image
# selects 4 images
