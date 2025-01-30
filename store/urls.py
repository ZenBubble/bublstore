from django.urls import path

from . import views

app_name = "store"
urlpatterns = [
    # /store/
    path("", views.IndexView.as_view(), name="index"),
    # /store/{{ item_id }}/
    path("<int:item_id>", views.detail, name="detail"),
    # /store/login/
    path("login", views.login, name="login"),
    # /store/register/
    path("register", views.register, name="register"),
]