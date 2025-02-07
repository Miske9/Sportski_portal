from rest_framework import serializers
from .models import *

class NatjecanjeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Natjecanje
        fields = ['id', 'naziv', 'datum_pocetka', 'datum_zavrsetka']

class TimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tim
        fields = ['id', 'naziv', 'grad', 'natjecanje']

class UtakmicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utakmica
        fields = ['id', 'natjecanje', 'datum', 'tim1', 'tim2', 'rezultat_tim1', 'rezultat_tim2']

class IgracSerializer(serializers.ModelSerializer):
    class Meta:
        model = Igrac
        fields = ['id', 'ime', 'prezime', 'tim', 'broj_dresa']
