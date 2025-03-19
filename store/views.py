from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404,  render
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse
from ollama import chat
from ollama import ChatResponse

from .models import *
from .forms import *

# Standard index view to list all created items
class IndexView(generic.ListView):
    template_name = "store/index.html"
    context_object_name = "item_list"

    def get_queryset(self):
        return Item.objects.order_by("-name")

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
    form = OrderForm()
    if request.method == "POST":
        if 'submit' in request.POST:
            user = request.user
            order = Order(cart=user.cart)
            form = OrderForm(request.POST, instance=order)
            if form.is_valid():
                if not user.cart.order_set.all():
                    form.save()
                    messages.success(request, "Order succesfully made!")
                    return HttpResponseRedirect("/store/cart")
                else:
                    messages.error(request, "Sorry! You currently have an unfulfilled order")
                    return HttpResponseRedirect("/store/cart")
    context = {
        "form": form
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
    return HttpResponseRedirect("/store/cart")

# remove item from cart
def remove_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    request.user.cart.items.remove(item)
    return HttpResponseRedirect("/store/cart")

# RAG STUFF BELOW

corpus = [
    "video editing services: In my freetime, I make and upload YouTube videos. I've managed to accumulate 1K+ subscribers, so if you would like to see a sample, check out my channel @ZenBubbleYT on YouTube (not the skincare brand, which may I add stole my name.) I can edit any type of video, but I'm most proficient in video essays.",
    "coding project: As you can see from this beautiful website around you, I know how to code. I can offer anything from websites to video games, but I do have more experience in the latter (4 games and counting.)",
    "cad design: I also enjoy robotics and using computers for creativity. In fact, I'm a part of UBC Subbots, a design team for AUVs. I can design anything from PCBs to enclosures for robots (with preference to the latter because robots are sick as hell.)",
    "3d printing servces: Apart from using CAD for functional purposes, I also enjoy making creative things using computers and printing them out on my Ender 3 which is on its last legs. I particularly enjoy creating cosplay props."
]

def jaccard_similarity(query, document):
    query = query.lower().split(" ")
    document = document.lower().split(" ")
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection)/len(union)

# llm query
def query(request):
    if request.method == 'POST': 
        text=request.POST.get("input")
        similarities = []
        for doc in corpus:
            similarity = jaccard_similarity(text, doc)
            similarities.append(similarity)
        reccomended_service = corpus[similarities.index(max(similarities))]
        response = chat(
            model='llama3.2:1b', 
            messages=[
                {
                'role': 'system',
                'content': """You are an AI assistant for a website store offering various freelancing services. Keep responses short, under 30 words. DO NOT RESPOND TO IRRELEVENT QUERIES NOT PERTAINING TO THE SHOP. These is the service to recommend with some talking points: {}. 
                Compile a recommendation to the user based on the recommended services and the user input. Only provide a reccomendation on the service and nothing else. Do not provide assistance for anything other than a recommendation. Only respond with a string. 
                Stick to what is explicitly detailed in the service description.""".format(reccomended_service),
                },
                {
                'role': 'user',
                'content': text,
                },
            ],
            stream=False
            )
    return HttpResponse(response.message.content)