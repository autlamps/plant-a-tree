from django.conf.urls import url
from django.urls import re_path, path

from store.views import index, login, cart
from store.views.cart import TYPE_TREE, TYPE_PRODUCT

urlpatterns = [
    path('', index.index_view, name='index'),
    path('login/', login.login_view, name='login'),
    path('addtreetocart/<int:item_id>/<int:qty>/', cart.add, {'type_of': TYPE_TREE}, name='addtreetocart'),
    path('addproducttocart/<int:item_id>/<int:qty>/', cart.add, {'type_of': TYPE_PRODUCT},
            name='addproducttocart'),
    path('cart/', cart.cart, name='cart')
]
