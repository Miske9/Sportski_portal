from django import forms # type: ignore
from .models import Natjecanje, Tim, Utakmica, Igrac

class NatjecanjeForm(forms.ModelForm):
    class Meta:
        model = Natjecanje
        fields = ['naziv', 'datum_pocetka', 'datum_zavrsetka']

class TimForm(forms.ModelForm):
    class Meta:
        model = Tim
        fields = ['naziv', 'grad', 'natjecanje']

class UtakmicaForm(forms.ModelForm):
    class Meta:
        model = Utakmica
        fields = ['natjecanje', 'datum', 'tim1', 'tim2', 'rezultat_tim1', 'rezultat_tim2']

class IgracForm(forms.ModelForm):
    class Meta:
        model = Igrac
        fields = ['ime', 'prezime', 'tim', 'broj_dresa']
