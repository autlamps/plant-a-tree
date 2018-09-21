from django.contrib import admin

from store.models import *

# Register your models here.
admin.register(Category)
admin.register(Tree)
admin.register(Product)
admin.register(Wishlist)
admin.register(WishlistTreeItem)
admin.register(WishlistProductItem)
admin.register(Cart)
admin.register(CartProductItem)
admin.register(CartTreeItem)