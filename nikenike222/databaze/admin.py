from django.contrib import admin
from .models import Kategorie, Velikosti, Sklad, Uzivatel, Tenisky, Objednavka

@admin.register(Kategorie)
class KategorieAdmin(admin.ModelAdmin):
    list_display = ("id_kategorie", "nazev_kategorie", "popis")
    search_fields = ("nazev_kategorie",)


@admin.register(Velikosti)
class VelikostiAdmin(admin.ModelAdmin):
    list_display = ("id_velikosti", "eu_velikost", "us_velikost")
    ordering = ("eu_velikost",)


@admin.register(Sklad)
class SkladAdmin(admin.ModelAdmin):
    list_display = ("id_sklad", "nazev_skladu", "mesto")
    search_fields = ("nazev_skladu", "mesto")


@admin.register(Uzivatel)
class UzivatelAdmin(admin.ModelAdmin):
    list_display = ("id_uzivatel", "jmeno", "prijmeni", "email", "role")
    search_fields = ("jmeno", "prijmeni", "email")


@admin.register(Tenisky)
class TeniskyAdmin(admin.ModelAdmin):
    list_display = (
        "id_tenisky",
        "nazev_modelu",
        "id_kategorie",
        "id_velikosti",
        "id_sklad",
        "barva",
        "material",
        "cena",
        "mnozstvi",
        "dostupnost",
    )

    list_filter = (
        "id_kategorie",
        "id_velikosti",
        "id_sklad",
        "barva",
        "material",
        "dostupnost",
    )

    search_fields = ("nazev_modelu", "barva", "material")

@admin.register(Objednavka)
class ObjednavkaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "jmeno_uzivatele",
        "tenisky",
        "sklad",
        "pocet",
        "datum"
    )

    list_filter = (
        "uzivatel",
        "tenisky",
        "datum"
    )

    search_fields = (
        "uzivatel__username",
        "uzivatel__first_name",
        "uzivatel__last_name",
        "tenisky__nazev_modelu"
    )

    def jmeno_uzivatele(self, obj):
        return f"{obj.uzivatel.first_name} {obj.uzivatel.last_name}"

    jmeno_uzivatele.short_description = "Uživatel"

    def sklad(self, obj):
        return obj.tenisky.id_sklad.nazev_skladu

    sklad.short_description = "Sklad"