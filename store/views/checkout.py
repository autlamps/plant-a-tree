import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from store.models import Cart


@login_required
def checkout(request):
    try:
        cart_ob = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return redirect('store:cart')

    total_cost = cart_ob.total_cost

    free_shipping = False

    if cart_ob.item_count > 10:
        free_shipping = True
    else:
        total_cost += 35

    return render(request, 'checkout.html', context={
        'page_title': 'Checkout',
        'trees': cart_ob.trees.all(),
        'products': cart_ob.products.all(),
        'total': total_cost,
        'free_shipping': free_shipping
    })


@login_required
@csrf_exempt
def process_checkout(request):
    cart_ob = Cart.objects.get(user=request.user)

    message = "Dear {}\n\n".format(request.POST["first_name"])
    message += "Thank you for your order. It will be dispatched at the " \
               "first " \
               "possible instant. Please find your order details below.\n\n"

    message += "QTY - PRODUCT NAME - COST\n"

    for tree_item in cart_ob.trees.all():
        message += "{} - {} - {}\n".format(tree_item.qty, tree_item.tree.name,
                                           tree_item.total_cost)

    for product_item in cart_ob.products.all():
        message += "{} - {} - {}\n".format(product_item.qty,
                                           product_item.product.name,
                                           product_item.total_cost)

    total_cost = cart_ob.total_cost

    if cart_ob.item_count > 10:
        message += "1 - SHIPPING - FREE\n\n"
    else:
        total_cost += 35
        message += "1 - SHIPPING - $35\n\n"

    message += "Total Cost: {}\n\n".format(total_cost)

    message += "Thanks\nJim"

    response = requests.post(
        "https://api.mailgun.net/v3/plantatree.xyz/messages",
        auth=("api", settings.MAILGUN_API_KEY),
        data={"from": "Jim Irrumabo <order@plantatree.xyz>",
              "to": [request.POST["email"]],
              "subject": "Thanks for ordering from Plant A Tree",
              "text": message})

    cart_ob.products.all().delete()
    cart_ob.trees.all().delete()

    return render(request, 'checkout_success.html')
