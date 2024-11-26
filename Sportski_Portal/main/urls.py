from django.urls import path # type: ignore
from . import views

app_name='main'

urlpatterns = [
    path('igraci/', views.igraci, name='igraci'),
    path('homepage/', views.homepage, name='homepage'),
    path('timovi/', views.timovi, name='timovi'),
    path('utakmice/', views.utakmice, name='utakmice'),
    path('natjecanja/', views.natjecanja, name='natjecanja'),
]
