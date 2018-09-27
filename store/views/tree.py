from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

from store.models import Tree


@require_http_methods(["GET"])
def get_tree(request, item_id):
    item = get_object_or_404(Tree, pk=item_id)
    return render(request, 'tree.html', context={
        'tree': item,
    })
