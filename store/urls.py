from django.urls import path

from . import views

app_name = "store"
urlpatterns = [
    # ex: /store/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /store/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /store/5/buy/
    path("<int:item_id>/review/", views.review, name="review"),
]