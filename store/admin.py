from django.contrib import admin

from .models import *

admin.site.register(WishList)

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Wishlist Info", {"fields": ["wishlist"]})
    ]
    inlines = [ReviewInline]
    list_display = ["name", "wishlist"]

admin.site.register(Item, ItemAdmin)
