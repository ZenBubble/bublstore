from django.contrib import admin

from .models import WishList, Item, User, Review

admin.site.register(WishList)

admin.site.register(Item)

admin.site.register(User)

admin.site.register(Review)