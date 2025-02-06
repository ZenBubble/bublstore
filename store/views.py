from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404,  render
from django.views import generic
from django.urls import reverse

from .models import *
from .forms import *

# Standard index view to list all created items
class IndexView(generic.ListView):
    template_name = "store/index.html"
    context_object_name = "item_list"

    def get_queryset(self):
        return Item.objects.order_by("name")[:5]

# Page for viewing a specific item, includes review functionality
def detail(request, item_id):
    # error page if we are accessing an item id that doesn't exist, most likely if it was manually inputted in url
    item = get_object_or_404(Item, pk=item_id)
    form = ReviewForm(instance=item) 
    if request.method == "POST":
        if 'submit' in request.POST:
            # create a review object with item and user fields already populated, so user doesn't have to manually select
            user = request.user
            review = Review(item=item, user=user)
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                messages.success(request, "Review added!")
                return HttpResponseRedirect(reverse("store:detail", args=(item.id,)))
    context = {
        "item": item,
        "form": form,
    }
    return render(request, "store/item.html", context)

# Log in page
def loginView(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/store")
        else:
            messages.info(request, "Username or password is incorrect")

    context = {
        'form': form
    }
    return render(request, "store/login.html", context)

# Register page
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        if 'submit' in request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account successfully created for " + user)
                return HttpResponseRedirect("login")
    context = {
        "form": form
    }
    return render(request, "store/register.html", context)

# cart page
def cart(request):
    context = {
    }
    return render(request, "store/cart.html", context)

## BELOW ARE FUNCTIONAL VIEWS, WHCIH MEANS THEY SHOULD NOT BE DIRECTLY ACCESSED BY THE USER

# Logout functionality
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/store")

# add item to cart
def add_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    request.user.cart.items.add(item)
    return HttpResponseRedirect("/store")

# remove item from cart
def remove_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    request.user.cart.items.remove(item)
    return HttpResponseRedirect("/store")