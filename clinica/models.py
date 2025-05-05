from django.db import models

# Create your models here.


class IdentificacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'identification', 'phone', 'email')
    search_fields = ('name', 'identification')
    list_filter = ('identification_type',)


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'species', 'breed', 'age', 'owner')
    search_fields = ('name', 'breed')
    list_filter = ('species',)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'pet', 'date', 'veterinarian')
    search_fields = ('pet__name', 'veterinarian')
    list_filter = ('date',)
    ordering = ('-date',)
