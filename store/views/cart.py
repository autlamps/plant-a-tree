from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseServerError, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods

from store.models import CartTreeItem, Cart, Tree, Product, CartProductItem

TYPE_TREE = 'tree'
TYPE_PRODUCT = 'product'


@login_required
@require_http_methods(["GET"])
@transaction.atomic
def add(request, type_of, item_id, qty):
    """"
    add: adds an item to the users cart

    NB: not currently a fan of this GET a specific URL implementation
    but it makes it easier to implement on the product page and
    speed is more important anyway.
    """
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart(user=request.user)
        cart.save()

    if type_of == TYPE_TREE:
        item = get_object_or_404(Tree, pk=item_id)

        # try and see if the item is already in the cart
        cart_item = CartTreeItem.objects.filter(tree=item, cart=cart).first()

        # otherwise create a new one
        if cart_item is None:
            cart_item = CartTreeItem(
                cart=cart,
                tree=item,
                qty=qty
            )
        else:
            cart_item.qty += qty

        cart_item.save()

        return render(request, 'addtocart.html', context={
            'image': item.year_one,
            'item_name': item.name,
            'item_qty': qty,
            'page_title': "Item Added To Cart"
        })

    elif type_of == TYPE_PRODUCT:
        item = get_object_or_404(Product, pk=item_id)

        cart_item = CartProductItem.objects.filter(product=item,
                                                   cart=cart).first()

        if cart_item is None:
            cart_item = CartProductItem(
                cart=cart,
                product=item,
                qty=qty
            )
        else:
            cart_item.qty += qty

        cart_item.save()

        return render(request, 'addtocart.html', context={
            'image': item.image,
            'item_name': item.name,
            'item_qty': qty,
            'page_title': "Item Added To Cart"
        })

    else:
        return HttpResponseServerError()


@login_required
@require_http_methods(["GET"])
def increase_tree_qty(request, item_id):
    item = get_object_or_404(CartTreeItem, pk=item_id)
    item.qty += 1
    item.save()
    return redirect('store:cart')


@login_required
@require_http_methods(["GET"])
def decrease_tree_qty(request, item_id):
    item = get_object_or_404(CartTreeItem, pk=item_id)
    item.qty += -1
    item.save()
    return redirect('store:cart')


@login_required
@require_http_methods(["GET"])
def remove_tree(request, item_id):
    item = get_object_or_404(CartTreeItem, pk=item_id)
    item.delete()
    return redirect('store:cart')


@login_required
@require_http_methods(["GET"])
def increase_product_qty(request, item_id):
    item = get_object_or_404(CartProductItem, pk=item_id)
    item.qty += 1
    item.save()
    return redirect('store:cart')


@login_required
@require_http_methods(["GET"])
def decrease_product_qty(request, item_id):
    item = get_object_or_404(CartProductItem, pk=item_id)
    item.qty += -1
    item.save()
    return redirect('store:cart')


@login_required
@require_http_methods(["GET"])
def remove_product(request, item_id):
    item = get_object_or_404(CartProductItem, pk=item_id)
    item.delete()
    return redirect('store:cart')


@login_required
@require_http_methods(["GET"])
def cart(request):
    try:
        cart_ob = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart_ob = Cart(user=request.user)
        cart_ob.save()

    return render(request, 'cart.html', context={
        'page_title': 'Cart',
        'trees': cart_ob.trees.all(),
        'products': cart_ob.products.all(),
    })
