from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def homepage(request):
    return HttpResponse('Welcome to homepage! <strong>#samoOIRI</strong>')
    