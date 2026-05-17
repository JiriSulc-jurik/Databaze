from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tenisky/", views.tenisky, name="tenisky"),
    path("kategorie/", views.kategorie, name="kategorie"),
    path("sklad/", views.sklad, name="sklad"),
    path("objednat/<int:id>/", views.objednat, name="objednat"),
    path("uzivatele/", views.uzivatele, name="uzivatele"),
]