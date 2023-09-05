from django.db.models.query import QuerySet

from .filters import (
    BaseClientFilter,
    BaseParcelFilter,
    BaseTruckFilter, 
    BaseDriverFilter,
    BaseLocationFilter,
    BaseShipmentFilter
)
from .models import (
    Client, Driver, Parcel, 
    Truck, Location, Shipment
)

def client_list(*, filters=None) -> QuerySet[Client]:
    filters = filters or {}

    qs = Client.objects.all()

    return BaseClientFilter(filters, qs).qs


def parcel_list(*, filters=None) -> QuerySet[Parcel]:
    filters = filters or {}

    qs = Parcel.objects.all()

    return BaseParcelFilter(filters, qs).qs


def truck_list(*, filters=None) -> QuerySet[Parcel]:
    filters = filters or {}

    qs = Truck.objects.all()

    return BaseTruckFilter(filters, qs).qs


def driver_list(*, filters=None) -> QuerySet[Parcel]:
    filters = filters or {}

    qs = Driver.objects.all()

    return BaseDriverFilter(filters, qs).qs


def location_list(*, filters=None) -> QuerySet[Parcel]:
    filters = filters or {}

    qs = Location.objects.all()

    return BaseLocationFilter(filters, qs).qs


def shipment_list(*, filters=None) -> QuerySet[Parcel]:
    filters = filters or {}

    qs = Shipment.objects.all()

    return BaseShipmentFilter(filters, qs).qs
