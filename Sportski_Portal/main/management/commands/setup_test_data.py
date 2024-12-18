import random

from django.db import transaction # type: ignore
from django.core.management.base import BaseCommand # type: ignore

from main.models import Natjecanje, Tim, Utakmica, Igrac
from main.factory import (
    NatjecanjeFactory,
    TimFactory,
    UtakmicaFactory,
    IgracFactory
)

NUM_NATJECANJA = 4
NUM_TIM = 8
NUM_UTAKMICA = 32
NUM_IGRACA = 40

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Natjecanje, Tim, Utakmica, Igrac]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_NATJECANJA):
            natjecanje = NatjecanjeFactory()

        for _ in range(NUM_TIM):
            tim = TimFactory()
        
        for _ in range(NUM_UTAKMICA):
            utakmica = UtakmicaFactory()
        
        for _ in range(NUM_IGRACA):
            igrac = IgracFactory()  
        