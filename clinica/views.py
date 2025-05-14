from rest_framework import viewsets
from .models import Identification, Owner, Pet, Appointment
from .serializers import (
    IdentificationSerializer, OwnerSerializer, PetSerializer, AppointmentSerializer
)

class IdentificationViewSet(viewsets.ModelViewSet):
    queryset = Identification.objects.all()
    serializer_class = IdentificationSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
