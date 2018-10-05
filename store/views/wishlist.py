from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseServerError, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods

from store.models import Wishlist, WishlistTreeItem, Tree, Product, WishlistProductItem

TYPE_TREE = 'tree'
TYPE_PRODUCT = 'product'


@login_required
@require_http_methods(["GET"])
@transaction.atomic
def add(request, type_of, item_id):
    """"
    add: adds an item to the users wishlist

    NB: not currently a fan of this GET a specific URL implementation
    but it makes it easier to implement on the product page and
    speed is more important anyway.
    """
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        wishlist = Wishlist(user=request.user)
        wishlist.save()

    if type_of == TYPE_TREE:
        item = get_object_or_404(Tree, pk=item_id)

        # try and see if the item is already in the wishlist
        wishlist_item = WishlistTreeItem.objects.filter(tree=item, wishlist=wishlist).first()

        # otherwise create a new one
        if wishlist_item is None:
            wishlist_item = WishlistTreeItem(
                wishlist=wishlist,
                tree=item,
            )

        wishlist_item.save()

        return render(request, 'addtowishlist.html', context={
            'image': item.year_one,
            'item_name': item.name,
            'page_title': "Item Added To wishlist"
        })

    elif type_of == TYPE_PRODUCT:
        item = get_object_or_404(Product, pk=item_id)

        wishlist_item = WishlistProductItem.objects.filter(product=item,
                                                   wishlist=wishlist).first()

        if wishlist_item is None:
            wishlist_item = WishlistProductItem(
                wishlist=wishlist,
                product=item,
            )

        wishlist_item.save()

        return render(request, 'addtowishlist.html', context={
            'image': item.image,
            'item_name': item.name,
            'page_title': "Item Added To wishlist"
        })

    else:
        return HttpResponseServerError()


@login_required
@require_http_methods(["GET"])
def remove_product(request, item_id):
    item = get_object_or_404(WishlistProductItem, pk=item_id)
    item.delete()
    return redirect('store:wishlist')


@login_required
@require_http_methods(["GET"])
def remove_tree(request, item_id):
    item = get_object_or_404(WishlistTreeItem, pk=item_id)
    item.delete()
    return redirect('store:wishlist')


@login_required
@require_http_methods(["GET"])
def wishlist(request):
    try:
        wishlist_ob = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        wishlist_ob = Wishlist(user=request.user)
        wishlist_ob.save()

    return render(request, 'wishlist.html', context={
        'page_title': 'Wishlist',
        'trees': wishlist_ob.trees.all(),
        'products': wishlist_ob.products.all(),
    })
