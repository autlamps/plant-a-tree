from django.conf.urls import url
from django.urls import re_path, path

from store.views import index, login, cart
from store.views.cart import TYPE_TREE, TYPE_PRODUCT

urlpatterns = [
    path('', index.index_view, name='index'),
    path('login/', login.login_view, name='login'),
    path('addtreetocart/<int:item_id>/<int:qty>/', cart.add,
         {'type_of': TYPE_TREE}, name='addtreetocart'),
    path('addproducttocart/<int:item_id>/<int:qty>/', cart.add,
         {'type_of': TYPE_PRODUCT}, name='addproducttocart'),
    path('cart/', cart.cart, name='cart'),
    path('carttreeadd/<int:item_id>/', cart.increase_tree_qty,
         name='increase_tree_qty'),
    path('carttreeremove/<int:item_id>/', cart.decrease_tree_qty,
         name='decrease_tree_qty'),
    path('carttreedelete/<int:item_id>/', cart.remove_tree,
         name='remove_tree'),
    path('cartproductadd/<int:item_id>/', cart.increase_product_qty,
         name='increase_product_qty'),
    path('cartproductremove/<int:item_id>/', cart.decrease_product_qty,
         name='decrease_product_qty'),
    path('cartproductdelete/<int:item_id>/', cart.remove_product,
         name='remove_product'),
]
