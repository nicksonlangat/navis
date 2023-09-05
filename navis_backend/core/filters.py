import django_filters
from .models import Client, Driver, Location, Parcel, Truck, Shipment

class BaseClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = ("id", "email", "phone_number")


class BaseParcelFilter(django_filters.FilterSet):
    class Meta:
        model = Parcel
        fields = ("id", "parcel_number", "status", "destination")


class BaseTruckFilter(django_filters.FilterSet):
    class Meta:
        model = Truck
        fields = ("id", "chasis_number", "registration_number")


class BaseDriverFilter(django_filters.FilterSet):
    class Meta:
        model = Driver
        fields = ("id", "licence_number", "identity_number")


class BaseLocationFilter(django_filters.FilterSet):
    class Meta:
        model = Location
        fields = ("id", "name")


class BaseShipmentFilter(django_filters.FilterSet):
    class Meta:
        model = Shipment
        fields = ("id", "shipment_number", "route_from", "route_to")
