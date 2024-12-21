from django.urls import path # type: ignore
from . import views
from main.views import *

app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path("logout/", views.logout_view, name='logout'),
    path("register/",views.register, name="register"),
    path("admin-korisnik/", views.admin_korisnik, name="admin_korisnik"),
    path('timovi/', TimListView.as_view(), name='tim-list'),
    path('timovi/<int:pk>/', TimDetailView.as_view(),name='tim-detail'),
    path('timovi/novo/', views.TimCreateView.as_view(), name='tim-create'),
    path('timovi/<int:pk>/uredi/', views.TimUpdateView.as_view(), name='tim-update'),
    path('timovi/<int:pk>/obrisi/', views.TimDeleteView.as_view(), name='tim-delete'),
    path('igraci/', IgracListView.as_view(), name='igrac-list'),
    path('igraci/<int:pk>/', IgracDetailView.as_view(), name='igrac-detail'),
    path('igraci/novo/', views.IgracCreateView.as_view(), name='igrac-create'),
    path('igraci/<int:pk>/uredi/', views.IgracUpdateView.as_view(), name='igrac-update'),
    path('igraci/<int:pk>/obrisi/', views.IgracDeleteView.as_view(), name='igrac-delete'),
    path('utakmice/', UtakmicaListView.as_view(), name='utakmica-list'),
    path('utakmice/<int:pk>/', UtakmicaDetailView.as_view(), name='utakmica-detail'),
    path('utakmice/novo/', views.UtakmicaCreateView.as_view(), name='utakmica-create'),
    path('utakmice/<int:pk>/uredi/', views.UtakmicaUpdateView.as_view(), name='utakmica-update'),
    path('utakmice/<int:pk>/obrisi/', views.UtakmicaDeleteView.as_view(), name='utakmica-delete'),
    path('natjecanja/', NatjecanjeListView.as_view(), name='natjecanje-list'),
    path('natjecanja/<int:pk>/', NatjecanjeDetailView.as_view(), name='natjecanje-detail'),
    path('natjecanja/novo/', views.NatjecanjeCreateView.as_view(), name='natjecanje-create'),
    path('natjecanja/<int:pk>/uredi/', views.NatjecanjeUpdateView.as_view(), name='natjecanje-update'),
    path('natjecanja/<int:pk>/obrisi/', views.NatjecanjeDeleteView.as_view(), name='natjecanje-delete'),
] 
