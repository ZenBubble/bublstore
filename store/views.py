from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import *


class IndexView(generic.ListView):
    template_name = "store/index.html"
    context_object_name = "item_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Item.objects.order_by("name")[:5]

class DetailView(generic.DetailView):
    model = Item
    template_name = "store/item.html"

# def buy(request, item_id): # example custom request for a new page
#     item = get_object_or_404(Item, pk=item_id)
#     context = {
#         "item": item,
#     }
#     return render(request, "store/buy.html", context) # request, template uri, context

def review(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        "item": item,
    }
    return render(request, "store/item.html", context)