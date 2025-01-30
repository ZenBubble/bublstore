from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404,  render
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
            # create a review object with item and user filled in, so user doesn't have to manually select
            user = request.user
            review = Review(item=item, user=user)
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("store:detail", args=(item.id,)))
    context = {
        "item": item,
        "form": form,
    }
    return render(request, "store/item.html", context) # request, template uri, context

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

def logoutView(request):
    logout(request)
    return HttpResponseRedirect("/store")

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