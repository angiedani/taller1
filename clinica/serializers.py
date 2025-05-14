from rest_framework import serializers
from .models import Identification, Owner, Pet, Appointment

class IdentificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identification
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    tipo_identificacion = IdentificationSerializer(read_only=True)
    tipo_identificacion_id = serializers.PrimaryKeyRelatedField(
        queryset=Identification.objects.all(), source='tipo_identificacion', write_only=True
    )

    class Meta:
        model = Owner
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    propietario = OwnerSerializer(read_only=True)
    propietario_id = serializers.PrimaryKeyRelatedField(
        queryset=Owner.objects.all(), source='propietario', write_only=True
    )

    class Meta:
        model = Pet
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    mascota = PetSerializer(read_only=True)
    mascota_id = serializers.PrimaryKeyRelatedField(
        queryset=Pet.objects.all(), source='mascota', write_only=True
    )

    class Meta:
        model = Appointment
        fields = '__all__'
