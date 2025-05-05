from django.contrib import admin
from .models import Identification, Owner, Pet, Appointment

# Register your models here.

admin.site.register(Identification)
admin.site.register(Owner)
admin.site.register(Pet)
admin.site.register(Appointment)