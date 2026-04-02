from rest_framework import serializers
from .models import Kategorija, Obaveza

class KategorijaSerializer(serializers.ModelSerializer):
    obaveze = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Kategorija
        fields = ["id", "naziv", "opis", "boja", "obaveze"]

class ObavezaSerializer(serializers.ModelSerializer):
    kategorija_detalji = KategorijaSerializer(source="kategorija", read_only=True)
    class Meta:
        model = Obaveza
        fields = ["id", "naslov", "opis", "kategorija","kategorija_detalji", "kreirano","rok_za_zavrsetak",
        "zavrseno","prioritet"]