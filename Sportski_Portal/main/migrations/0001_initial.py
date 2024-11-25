# Generated by Django 5.1.2 on 2024-11-25 23:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Natjecanje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=200)),
                ('datum_pocetka', models.DateField()),
                ('datum_zavrsetka', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=200)),
                ('grad', models.CharField(max_length=100)),
                ('natjecanje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timovi', to='main.natjecanje')),
            ],
        ),
        migrations.CreateModel(
            name='Igrac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=100)),
                ('prezime', models.CharField(max_length=100)),
                ('broj_dresa', models.PositiveIntegerField()),
                ('tim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='igraci', to='main.tim')),
            ],
        ),
        migrations.CreateModel(
            name='Utakmica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateTimeField()),
                ('rezultat_tim1', models.PositiveIntegerField(default=0)),
                ('rezultat_tim2', models.PositiveIntegerField(default=0)),
                ('natjecanje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utakmice', to='main.natjecanje')),
                ('tim1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utakmice_tim1', to='main.tim')),
                ('tim2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utakmice_tim2', to='main.tim')),
            ],
        ),
    ]
