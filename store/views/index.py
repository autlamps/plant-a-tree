import random

from django.shortcuts import render

from store.models import Tree


def index_view(request):
    # Get featured tree
    min = 1
    max = Tree.objects.count()
    if min == max:
        tree_number = min
    else:
        tree_number = random.randint(min, max)
    tree = Tree.objects.get(id=tree_number)
    # Get facts
    if max > 5:
        num_trees = 5
    else:
        num_trees = max
    facts = set()
    while len(facts) != num_trees:
        facts.update(Tree.objects.filter(id=random.randint(min, max)))
    facts_r = list(facts)
    random.shuffle(facts_r)
    trees = set()
    # Get all trees
    trees.update(Tree.objects.all())

    return render(request, 'index.html', context={
        'tree': tree,
        'trees': trees,
        'facts': facts_r,
        'page_title': "Home"
    })
