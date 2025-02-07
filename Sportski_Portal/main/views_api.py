from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class NatjecanjeViewSet(viewsets.ModelViewSet):
    queryset = Natjecanje.objects.all()
    serializer_class = NatjecanjeSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]

class TimViewSet(viewsets.ModelViewSet):
    queryset = Tim.objects.all()
    serializer_class = TimSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]

class UtakmicaViewSet(viewsets.ModelViewSet):
    queryset = Utakmica.objects.all()
    serializer_class = UtakmicaSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]

class IgracViewSet(viewsets.ModelViewSet):
    queryset = Igrac.objects.all()
    serializer_class = IgracSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]
