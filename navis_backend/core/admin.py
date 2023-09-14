from django.contrib import admin
from .models import Client, Parcel, Driver, Truck, Shipment, Location

# Register your models here.

admin.site.register(Client)
admin.site.register(Parcel)
admin.site.register(Driver)
admin.site.register(Truck)
admin.site.register(Shipment)
admin.site.register(Location)
