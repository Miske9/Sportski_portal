import factory
from factory.django import DjangoModelFactory  # type: ignore
from django.utils import timezone  # type: ignore
import random
from main.models import Natjecanje, Tim, Utakmica, Igrac

class NatjecanjeFactory(DjangoModelFactory):
    class Meta:
        model = Natjecanje

    naziv = factory.Faker("last_name")  
    datum_pocetka = factory.Faker("date_this_decade")  
    datum_zavrsetka = factory.Faker("date_this_decade")  

    @factory.lazy_attribute
    def datum_zavrsetka(self):
        
        return self.datum_pocetka + timezone.timedelta(days=random.randint(30, 365))

def setup_natjecanja():
    
    if Natjecanje.objects.count() < 4:
        for _ in range(4 - Natjecanje.objects.count()):
            NatjecanjeFactory.create()
    return Natjecanje.objects.all()[:4]

natjecanja = setup_natjecanja()

class TimFactory(DjangoModelFactory):
    class Meta:
        model = Tim

    naziv = factory.Faker("last_name")  
    grad = factory.Faker("city")  
    natjecanje = factory.Iterator(natjecanja)  

class UtakmicaFactory(DjangoModelFactory):
    class Meta:
        model = Utakmica

    natjecanje = factory.Iterator(natjecanja)  
    datum = factory.Faker("date_time_this_year", tzinfo=timezone.get_current_timezone())  
    tim1 = factory.SubFactory(TimFactory)  
    tim2 = factory.SubFactory(TimFactory)  

    @factory.lazy_attribute
    def tim1(self):
        return random.choice(Tim.objects.all())  
    
    @factory.lazy_attribute
    def tim2(self):
        tim1 = self.tim1
        tim2 = random.choice(Tim.objects.exclude(id=tim1.id))  
        return tim2

    rezultat_tim1 = factory.Faker('random_int', min=0, max=9)  
    rezultat_tim2 = factory.Faker('random_int', min=0, max=9)  

class IgracFactory(DjangoModelFactory):
    class Meta:
        model = Igrac

    ime = factory.Faker("first_name")  
    prezime = factory.Faker("last_name")  
    tim = factory.SubFactory(TimFactory)  
    broj_dresa = factory.Faker("random_int", min=1, max=99)  

    @factory.lazy_attribute
    def tim(self):
        
        return random.choice(Tim.objects.all())
