from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tenisky, Kategorie, Sklad, Uzivatel, Objednavka


def index(request):
    return render(request, "databaze/index.html", {
        "pocet_tenisek": Tenisky.objects.count(),
        "pocet_kategorii": Kategorie.objects.count(),
        "pocet_skladu": Sklad.objects.count(),
        "pocet_kusu": sum(t.mnozstvi for t in Tenisky.objects.all()),
    })


def tenisky(request):
    hledat = request.GET.get("hledat", "")
    kategorie_id = request.GET.get("kategorie", "")

    tenisky = Tenisky.objects.all()
    kategorie = Kategorie.objects.all()

    if hledat:
        tenisky = tenisky.filter(nazev_modelu__icontains=hledat)

    if kategorie_id:
        tenisky = tenisky.filter(id_kategorie_id=kategorie_id)

    return render(request, "databaze/tenisky.html", {
        "tenisky": tenisky,
        "kategorie": kategorie,
        "hledat": hledat,
        "vybrana_kategorie": kategorie_id,
    })


def kategorie(request):
    return render(request, "databaze/kategorie.html", {
        "kategorie": Kategorie.objects.all()
    })


def sklad(request):
    return render(request, "databaze/sklad.html", {
        "sklad": Sklad.objects.all()
    })


@login_required
def objednat(request, id):
    teniska = get_object_or_404(Tenisky, pk=id)

    if teniska.mnozstvi > 0:
        teniska.mnozstvi -= 1

        if teniska.mnozstvi == 0:
            teniska.dostupnost = "NE"
        else:
            teniska.dostupnost = "ANO"

        teniska.save()

        Objednavka.objects.create(
            uzivatel=request.user,
            tenisky=teniska,
            pocet=1
        )

    return redirect("tenisky")


@login_required
def uzivatele(request):
    uzivatele = Uzivatel.objects.all()
    return render(request, "databaze/uzivatele.html", {
        "uzivatele": uzivatele
    })