import random

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from store.models import Tree


def index_view(request):
    min = 1
    max = Tree.objects.count()
    if min == max:
        tree_number = min
    else:
        tree_number = random.randint(min, max)

    tree = Tree.objects.get(id=tree_number)

    if max > 5:
        num_trees = 5
    else:
        num_trees = max

    facts = set()
    for i in range(num_trees):
        facts.update(Tree.objects.filter(id=random.randint(min, max)))
        if len(facts) is not i:
            num_trees + 1

    trees = set()

    trees.update(Tree.objects.all())

    return render(request, 'index.html', context={
        'tree': tree,
        'trees': trees,
        'facts': facts,
        'page_title': "Home"
    })
