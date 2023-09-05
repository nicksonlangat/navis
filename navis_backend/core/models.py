import string
import random
from django.db import models
from common.models import BaseModel


class Location(BaseModel):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return f"{self.name}"
    

class Truck(BaseModel):
    manufacturer = models.CharField(max_length=250, null=True, blank=True)
    model = models.CharField(max_length=250, null=True, blank=True)
    chasis_number = models.CharField(max_length=250, unique=True)
    registration_number = models.CharField(max_length=250, unique=True)
    engine_size = models.CharField(max_length=250, null=True, blank=True)
    engine_power = models.CharField(max_length=250, null=True, blank=True)
    yom = models.DateField(null=True, blank=True)
    carry_weight = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"


class Driver(BaseModel):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    licence_number = models.CharField(max_length=50, unique=True)
    identity_number = models.CharField(max_length=50, unique=True)
    kra_pin = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Client(BaseModel):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    identity_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Parcel(BaseModel):
    class Status(models.TextChoices):
        DELAYED = "DELAYED", "Delayed"
        ONWAY = "ON WAY", "On way"
        ARRIVED = "ARRIVED", "Arrived"
        
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    parcel_number = models.CharField(max_length=250, null=True, blank=True)
    weight = models.DecimalField(max_digits=9, decimal_places=2)
    item = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.ONWAY)
    destination = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    recipient_contact = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.parcel_number}"
    
    def save(self, *args, **kwargs):
        if not self.parcel_number:
            chars=string.ascii_uppercase + string.digits
            self.parcel_number = ''.join(random.choice(chars) for _ in range(6))
        super(Parcel, self).save(*args, **kwargs)


class Shipment(BaseModel):
    class Status(models.TextChoices):
        DELAYED = "DELAYED", "Delayed"
        ONWAY = "ON WAY", "On way"
        ARRIVED = "ARRIVED", "Arrived"
        
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    parcels = models.ManyToManyField(Parcel, blank=True)
    shipment_number = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.ONWAY)
    route_from = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    route_to = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="destination", null=True, blank=True)
    departure_date = models.DateTimeField(null=True, blank=True)
    arrival_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.shipment_number}"
    
    def save(self, *args, **kwargs):
        if not self.shipment_number:
            chars=string.ascii_uppercase + string.digits
            self.shipment_number = ''.join(random.choice(chars) for _ in range(6))
        super(Shipment, self).save(*args, **kwargs)

