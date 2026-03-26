from django.db import models
from django.utils import timezone

# Create your models here.
class Kategorija(models.Model):
    naziv = models.CharField(max_length=100)
    opis = models.TextField(blank=True, null=True)
    boja = models.CharField(max_length=7, default="#000000", help_text="HEX vrednost boje za UI")

    class Meta:
        verbose_name_plural = "kategorije"

    def __str__(self):
        return self.naziv

class Obaveza(models.Model):
    
    NIZAK = "N"
    SREDNJI = "S"
    VISOK = "V"
    PRIORITET_CHOICES = [
        {NIZAK, "Nizak"},
        {SREDNJI, "Srednji"},
        {VISOK, "Visok"}
    ]

    naslov = models.CharField(max_length=100)
    opis = models.TextField(blank=True, null=True)
    kreirano = models.DateTimeField(auto_now_add=True)
    rok_za_zavrsetak = models.DateTimeField(default=timezone.now)
    zavrseno = models.BooleanField(default=False)
    prioritet = models.CharField(max_length=7, choices=PRIORITET_CHOICES, default=SREDNJI)

    kategorija = models.ForeignKey(Kategorija, on_delete=models.SET_NULL, null=True,blank=True, related_name="obaveze")

    class Meta:
        verbose_name_plural = "Obaveze"

    def __str__(self):
        return self.naslov