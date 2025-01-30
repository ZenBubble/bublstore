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
    form = ReviewForm(instance=item)
    if request.method == "POST":
        if 'submit' in request.POST:
            # create a review object with item filled in, so user doesn't have to manually select
            review = Review(item=item)
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("store:detail", args=(item.id,)))
    context = {
        "item": item,
        "form": form,
    }
    return render(request, "store/item.html", context) # request, template uri, context

def login(request):
    context = {
    }
    return render(request, "store/login.html", context)

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        if 'submit' in request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("")
    context = {
        "form": form
    }
    return render(request, "store/register.html", context)