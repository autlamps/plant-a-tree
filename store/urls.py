from django.conf.urls import url
from django.urls import re_path, path

from store.views import index, login, cart, tree, product, wishlist
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
    path('tree/<int:item_id>/', tree.get_tree,
         name="get_tree"),
    path('product/<int:item_id>/', product.get_product,
         name="get_product"),
    path('addtreetowishlist/<int:item_id>/', wishlist.add,
         {'type_of': TYPE_TREE}, name='addtreetowishlist'),
    path('addproducttowishlist/<int:item_id>/', wishlist.add,
         {'type_of': TYPE_PRODUCT}, name='addproducttowishlist'),
    path('wishlist/', wishlist.wishlist, name='wishlist'),
    path('wishlistproductremove/<int:item_id>/', wishlist.remove_product,
         name='removeproductfromwishlist'),
    path('wishlisttreeremove/<int:item_id>/', wishlist.remove_tree,
         name='removetreefromwishlist'),
]
