from django.contrib import admin

from .models import *

admin.site.register(Cart)

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "cost"]}),
        # ("Cart Info", {"fields": ["cart"]})
    ]
    inlines = [ReviewInline]
    list_display = ["name", "cost", Item.num_review]

admin.site.register(Item, ItemAdmin)
