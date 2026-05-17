from django.db import models
from django.contrib.auth.models import User


class Kategorie(models.Model):
    id_kategorie = models.AutoField(primary_key=True)
    nazev_kategorie = models.CharField(max_length=255)
    popis = models.CharField(max_length=255)

    def __str__(self):
        return self.nazev_kategorie


class Velikosti(models.Model):
    id_velikosti = models.AutoField(primary_key=True)
    eu_velikost = models.IntegerField()
    us_velikost = models.IntegerField()

    def __str__(self):
        return str(self.eu_velikost)


class Sklad(models.Model):
    id_sklad = models.AutoField(primary_key=True)
    nazev_skladu = models.CharField(max_length=255)
    mesto = models.CharField(max_length=255)

    def __str__(self):
        return self.nazev_skladu


class Uzivatel(models.Model):
    id_uzivatel = models.AutoField(primary_key=True)
    jmeno = models.CharField(max_length=255)
    prijmeni = models.CharField(max_length=255)
    email = models.EmailField()
    role = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"


class Tenisky(models.Model):
    BARVA_CHOICES = [
        ("Černá", "Černá"),
        ("Bílá", "Bílá"),
        ("Modrá", "Modrá"),
        ("Zelená", "Zelená"),
        ("Červená", "Červená"),
        ("Šedá", "Šedá"),
        ("Hnědá", "Hnědá"),
        ("Oranžová", "Oranžová"),
        ("Žlutá", "Žlutá"),
    ]

    MATERIAL_CHOICES = [
        ("Textil", "Textil"),
        ("Kůže", "Kůže"),
        ("Síťovina", "Síťovina"),
        ("Syntetika", "Syntetika"),
        ("Recyklovaný materiál", "Recyklovaný materiál"),
    ]

    DOSTUPNOST_CHOICES = [
        ("ANO", "ANO"),
        ("NE", "NE"),
    ]

    id_tenisky = models.AutoField(primary_key=True)
    id_kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE)
    id_velikosti = models.ForeignKey(Velikosti, on_delete=models.CASCADE)
    id_sklad = models.ForeignKey(Sklad, on_delete=models.CASCADE)
    id_uzivatel = models.ForeignKey(Uzivatel, on_delete=models.CASCADE)

    nazev_modelu = models.CharField(max_length=255)
    barva = models.CharField(max_length=255, choices=BARVA_CHOICES)
    material = models.CharField(max_length=255, choices=MATERIAL_CHOICES)
    rok_vydani = models.IntegerField()
    cena = models.IntegerField()
    mnozstvi = models.IntegerField()
    dostupnost = models.CharField(max_length=10, choices=DOSTUPNOST_CHOICES)

    def __str__(self):
        return self.nazev_modelu

class Objednavka(models.Model):
    uzivatel = models.ForeignKey(User, on_delete=models.CASCADE)
    tenisky = models.ForeignKey(Tenisky, on_delete=models.CASCADE)
    pocet = models.IntegerField(default=1)
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uzivatel.username} objednal {self.tenisky.nazev_modelu}"