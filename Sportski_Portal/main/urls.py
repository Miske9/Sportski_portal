from django.urls import path # type: ignore
from . import views

app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path("register/",views.register, name="register"),
    path("admin-korisnik/", views.admin_korisnik, name="admin_korisnik"),
]
