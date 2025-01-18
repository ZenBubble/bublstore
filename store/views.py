from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.urls import reverse

from .models import *
from .forms import *


class IndexView(generic.ListView):
    template_name = "store/index.html"
    context_object_name = "item_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Item.objects.order_by("name")[:5]

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("store:detail", args=(item.id,)))
    else:
        form = ReviewForm()
    context = {
        "item": item,
        "form": form
    }
    return render(request, "store/item.html", context) # request, template uri, context

# def buy(request, item_id): # example custom request for a new page
#     item = get_object_or_404(Item, pk=item_id)
#     context = {
#         "item": item,
#     }
#     return render(request, "store/buy.html", context) # request, template uri, context
