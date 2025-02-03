from rest_framework import viewsets
from .serializers import NatjecanjeSerializer, TimSerializer, UtakmicaSerializer, IgracSerializer
from .models import Natjecanje, Tim, Utakmica, Igrac
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# API View za Natjecanje
class NatjecanjeViewSet(viewsets.ModelViewSet):
    queryset = Natjecanje.objects.all()
    serializer_class = NatjecanjeSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]

# API View za Tim
class TimViewSet(viewsets.ModelViewSet):
    queryset = Tim.objects.all()
    serializer_class = TimSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]

# API View za Utakmica
class UtakmicaViewSet(viewsets.ModelViewSet):
    queryset = Utakmica.objects.all()
    serializer_class = UtakmicaSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]

# API View za Igrac
class IgracViewSet(viewsets.ModelViewSet):
    queryset = Igrac.objects.all()
    serializer_class = IgracSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]
