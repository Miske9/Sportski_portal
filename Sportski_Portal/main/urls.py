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
    path('igraci/', IgracListView.as_view(), name='igrac-list'),
    path('igraci/<int:pk>/', IgracDetailView.as_view(), name='igrac-detail'),
    path('utakmice/', UtakmicaListView.as_view(), name='utakmica-list'),
    path('utakmice/<int:pk>/', UtakmicaDetailView.as_view(), name='utakmica-detail'),
    path('natjecanja/', NatjecanjeListView.as_view(), name='natjecanje-list'),
    path('natjecanja/<int:pk>/', NatjecanjeDetailView.as_view(), name='natjecanje-detail'),
] 
