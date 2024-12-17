from django.urls import path # type: ignore
from . import views
from main.views import *

app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path("register/",views.register, name="register"),
    path("admin-korisnik/", views.admin_korisnik, name="admin_korisnik"),
    path('timovi/', TimListView.as_view()),
    path('igraci/', IgracListView.as_view()),
    path('utakmice/', UtakmicaListView.as_view()),
    path('natjecanja/', NatjecanjeListView.as_view(), name='natjecanje-list'),
]
