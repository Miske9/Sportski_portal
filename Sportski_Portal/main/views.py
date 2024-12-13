from django.shortcuts import get_object_or_404  # type: ignore
from django.db.models import Q # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin # type: ignore
from django.shortcuts import render, redirect  # type: ignore
from django.http import HttpResponse  # type: ignore
from django.contrib.auth.forms import UserCreationForm  # type: ignore
from django.contrib.auth import authenticate, login, logout  # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.views.generic import ListView, DetailView  # type: ignore
from main.models import Natjecanje, Tim, Igrac, Utakmica

def index(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('/')

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

class NatjecanjeListView(LoginRequiredMixin,ListView):
    model = Natjecanje
    template_name = 'natjecanje_list.html'  
    context_object_name = 'natjecanja'
    paginate_by = 100

    def get_queryset(self):
        queryset = super().get_queryset()
        naziv = self.request.GET.get('naziv', None)
        datum_pocetka = self.request.GET.get('datum_pocetka', None)
        datum_zavrsetka = self.request.GET.get('datum_zavrsetka', None)

        if naziv:
            queryset = queryset.filter(naziv__icontains=naziv)
        if datum_pocetka:
            queryset = queryset.filter(datum_pocetka__gte=datum_pocetka)
        if datum_zavrsetka:
            queryset = queryset.filter(datum_zavrsetka__lte=datum_zavrsetka)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timovi'] = Tim.objects.all()
        context['utakmice'] = Utakmica.objects.all()
        return context

class NatjecanjeDetailView(LoginRequiredMixin,DetailView):
    model = Natjecanje
    template_name = 'main/natjecanje_detail.html'
    context_object_name = 'natjecanje'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        natjecanje = self.get_object()
        context['timovi'] = Tim.objects.filter(natjecanje=natjecanje)
        context['utakmice'] = Utakmica.objects.filter(natjecanje=natjecanje)

        return context

class TimListView(LoginRequiredMixin,ListView):
    model = Tim
    template_name = 'tim_list.html'
    context_object_name = 'timovi'

    def get_queryset(self):
        queryset = super().get_queryset()
        naziv = self.request.GET.get('naziv', None)
        grad = self.request.GET.get('grad', None)
        natjecanje_id = self.request.GET.get('natjecanje', None)

        if naziv:
            queryset = queryset.filter(naziv__icontains=naziv)
        if grad:
            queryset = queryset.filter(grad__icontains=grad)
        if natjecanje_id:
            queryset = queryset.filter(natjecanje__id=natjecanje_id)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['natjecanja'] = Natjecanje.objects.all()
        context['gradovi'] = Tim.objects.values_list('grad', flat=True).distinct()
        return context

class TimDetailView(LoginRequiredMixin,DetailView):
    model = Tim
    template_name = 'main/tim_detail.html'
    context_object_name = 'timovi'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        timovi = self.get_object()
        context['natjecanja'] = Natjecanje.objects.filter(timovi=timovi)

        return context

class UtakmicaListView(LoginRequiredMixin,ListView):
    model = Utakmica
    template_name = 'utakmica_list.html'
    context_object_name = 'utakmice'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        natjecanje_id = self.request.GET.get('natjecanje')
        if natjecanje_id:
            queryset = queryset.filter(natjecanje__id=natjecanje_id)
        
        tim_id = self.request.GET.get('tim')
        if tim_id:
            queryset = queryset.filter(Q(tim1__id=tim_id) | Q(tim2__id=tim_id))
        
        datum_od = self.request.GET.get('datum_od')
        datum_do = self.request.GET.get('datum_do')
        if datum_od and datum_do:
            queryset = queryset.filter(datum__range=[datum_od, datum_do])
        elif datum_od:
            queryset = queryset.filter(datum__gte=datum_od)
        elif datum_do:
            queryset = queryset.filter(datum__lte=datum_do)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['natjecanja'] = Natjecanje.objects.all()
        context['timovi'] = Tim.objects.all()
        return context

class UtakmicaDetailView(LoginRequiredMixin,DetailView):
    model = Utakmica
    template_name = 'main/utakmica_detail.html'
    context_object_name = 'utakmice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        utakmice = self.get_object()
        context['natjecanje'] = Natjecanje.objects.filter(utakmice=utakmice)        
      
        return context  
      
class IgracListView(LoginRequiredMixin,ListView):
    model = Igrac
    template_name = 'igrac_list.html'
    context_object_name = 'igraci'

    def get_queryset(self):
        queryset = super().get_queryset()
        ime = self.request.GET.get('ime', None)
        prezime = self.request.GET.get('prezime', None)
        tim_id = self.request.GET.get('tim', None)
        broj_dresa = self.request.GET.get('broj_dresa', None)

        if ime:
            queryset = queryset.filter(ime__icontains=ime)
        if prezime:
            queryset = queryset.filter(prezime__icontains=prezime)
        if tim_id:
            queryset = queryset.filter(tim__id=tim_id)
        if broj_dresa:
            queryset = queryset.filter(broj_dresa=broj_dresa)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timovi'] = Tim.objects.all()
        return context

class IgracDetailView(LoginRequiredMixin,DetailView):
    model = Igrac
    template_name = 'main/igrac_detail.html'
    context_object_name = 'igraci'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        igraci = self.get_object()
        context['timovi'] = Tim.objects.filter(igraci=igraci)

        return context
 



 
    