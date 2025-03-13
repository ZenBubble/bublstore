from django.urls import path
from . import views

app_name = "store"
urlpatterns = [
    # /store/
    path("", views.IndexView.as_view(), name="index"),
    # /store/{{ item_id }}/
    path("<int:item_id>", views.detail, name="detail"),
    # /store/login/
    path("login", views.loginView, name="login"),
    # /store/register/
    path("register", views.register, name="register"),
    # /store/cart
    path("cart", views.cart, name="cart"),

    # BELOW ARE FUNCTIONAL VIEWS, WHICH MEANS THEY SHOULD NOT BE DIRECTLY ACCESSED BY THE USER

    # logout user
    path("logout", views.logout_user, name="logout"),

    # add item to cart
    path("add_cart/<int:item_id>", views.add_cart, name="add_cart"),

    # remove item from cart
    path("remove_cart/<int:item_id>", views.remove_cart, name="remove_cart"),

    # llm query
    path("query", views.query, name="query"),
]
