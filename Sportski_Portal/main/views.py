from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def homepage(request):
    return render(request, 'homepage.html')

def igraci(request):
    return render(request, 'igraci.html')

def timovi(request):
    return render(request, 'timovi.html')

def utakmice(request):
    return render(request, 'utakmice.html')

def natjecanja(request):
    return render(request, 'natjecanja.html')

    