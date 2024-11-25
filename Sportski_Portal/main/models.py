from django.db import models # type: ignore

class Natjecanje(models.Model):
    naziv = models.CharField(max_length=200)
    datum_pocetka = models.DateField()
    datum_zavrsetka = models.DateField()

    def __str__(self):
        return self.naziv
    
    class Meta:
        db_table = "natjecanje"
        verbose_name = "Natjecanje"
        verbose_name_plural = "Natjecanja"

class Tim(models.Model):
    naziv = models.CharField(max_length=200)
    grad = models.CharField(max_length=100)
    natjecanje = models.ForeignKey(Natjecanje, on_delete=models.CASCADE, related_name='timovi')

    def __str__(self):
        return self.naziv
    
    class Meta:
        db_table = "tim"
        verbose_name = "Tim"
        verbose_name_plural = "Timovi"

class Utakmica(models.Model):
    natjecanje = models.ForeignKey(Natjecanje, on_delete=models.CASCADE, related_name='utakmice')
    datum = models.DateTimeField()
    tim1 = models.ForeignKey(Tim, on_delete=models.CASCADE, related_name='utakmice_tim1')
    tim2 = models.ForeignKey(Tim, on_delete=models.CASCADE, related_name='utakmice_tim2')
    rezultat_tim1 = models.PositiveIntegerField(default=0)
    rezultat_tim2 = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.tim1} vs {self.tim2} - {self.datum}"
    
    class Meta:
        db_table = "utakmica"
        verbose_name = "Utakmica"
        verbose_name_plural = "Utakmice"

class Igrac(models.Model):
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    tim = models.ForeignKey(Tim, on_delete=models.CASCADE, related_name='igraci')
    broj_dresa = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.ime} {self.prezime} ({self.tim})"
    
    class Meta:
        db_table = "igrac"
        verbose_name = "Igrac"
        verbose_name_plural = "Igraci"
