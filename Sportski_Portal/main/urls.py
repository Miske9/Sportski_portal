from django.urls import path # type: ignore
from . import views

app_name='main'

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
]
