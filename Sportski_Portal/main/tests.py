from django.test import TestCase
from main.models import Natjecanje, Tim, Utakmica

class ModelTest(TestCase):

    def setUp(self):
        self.natjecanje = Natjecanje.objects.create(
            naziv="Liga Prvaka",
            datum_pocetka="2025-06-01",
            datum_zavrsetka="2025-06-30"
        )
        self.tim1 = Tim.objects.create(
            naziv="Jupiter",
            grad="Zagreb",
            natjecanje=self.natjecanje
        )
        self.tim2 = Tim.objects.create(
            naziv="Stewart",
            grad="Varazdin",
            natjecanje=self.natjecanje
        )
        self.utakmica = Utakmica.objects.create(
            natjecanje=self.natjecanje,
            tim1=self.tim1,
            tim2=self.tim2,
            datum="2024-06-10 18:00:00",
            rezultat_tim1=5,
            rezultat_tim2=1
        )

    def test_naziv_natjecanja_str(self):
        self.assertEqual(str(self.natjecanje), "Liga Prvaka")

    def test_tim_str(self):
        self.assertEqual(str(self.tim1), "Jupiter")

    def test_utakmica_str(self):
        self.assertEqual(str(self.utakmica), "Jupiter vs Stewart - 2024-06-10 18:00:00")
