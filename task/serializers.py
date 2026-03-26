from rest_framework import serializers
from .models import Kategorija, Obaveza

class KategorijaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategorija
        fields = ["id", "naziv", "opis", "boja", "obaveze"]
        obaveze = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

class ObavezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obaveza
        fields = ["id", "naslov", "opis", "kategorija", "kreirano","rok_za_zavrsetak",
        "zavrseno","prioritet"]