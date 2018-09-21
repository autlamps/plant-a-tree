from django.contrib import admin

from store.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Tree)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(WishlistTreeItem)
admin.site.register(WishlistProductItem)
admin.site.register(Cart)
admin.site.register(CartProductItem)
admin.site.register(CartTreeItem)
