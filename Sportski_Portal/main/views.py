from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
from django.contrib.auth.decorators import login_required# type: ignore

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

def is_staff_provjera(user):
    return user.is_staff

@login_required
def admin_korisnik(request):
    if not request.user.is_staff:
        return HttpResponse("Nemate prava za ovu stranicu.")
    return render(request, "admin_korisnik.html")