from django.db import models

# Create your models here.


class Identification(models.Model):
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Owner(models.Model):
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    tipo_identificacion = models.ForeignKey(Identification, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class Pet(models.Model):
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20, unique=True) 
    correo = models.EmailField(blank=True, null=True)  
    telefono = models.CharField(max_length=20, blank=True)  
    direccion = models.CharField(max_length=200, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True)
    edad = models.PositiveIntegerField()
    propietario = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Appointment(models.Model):
    nombre = models.CharField(max_length=100) 
    identificacion = models.CharField(max_length=20, unique=True)  
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    mascota = models.ForeignKey(Pet, on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField()
    motivo = models.TextField()
    veterinario = models.CharField(max_length=100)

    def __str__(self):
        return f"Cita {self.identificacion} - {self.mascota.nombre}"
