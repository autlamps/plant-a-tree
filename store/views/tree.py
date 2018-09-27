from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

from store.models import Tree


@require_http_methods(["GET"])
def get_tree(request, item_id):
    item = get_object_or_404(Tree, pk=item_id)
    return render(request, 'tree.html', context={
        'name': item.name,
        'maintenance': item.maintenance,
        'growth': item.growth_rate,
        'category': item.category,
        'description': item.description,
        'facts': item.fun_facts,
        'height': item.height,
        'y1': item.year_one,
        'y2': item.year_two,
        'y3': item.year_three,
        'y5': item.year_five,
        'y10': item.year_ten,
        'tree': item,
    })
