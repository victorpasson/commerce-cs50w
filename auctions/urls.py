from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("categories/<int:cat_id>", views.categories, name="categorie"),
    path("auction/<int:auction_id>", views.auction, name="auction"),
    path("auction/<int:auction_id>/comment", views.comment, name="comment"),
    path("auction/close", views.close, name="close"),
    path("create", views.create, name="create"),
    path("watch", views.watch, name="watch"),
]
