from django.urls import path # type: ignore
from . import views

app_name = 'main'  

urlpatterns = [
    path('', views.homepage, name='homepage'),
]