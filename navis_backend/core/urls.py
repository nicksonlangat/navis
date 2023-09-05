from django.urls import path

from .views import (
    ClientApi, TruckApi, DriverApi,
    ShipmentApi, ParcelApi, LocationApi,
    AnalyticsApi
    )

urlpatterns = [
    # client endpoints
    path("clients", ClientApi.as_view(), name="clients"),
    path("clients/<uuid:pk>/", ClientApi.as_view(), name="client"),

    # truck endpoints
    path("trucks", TruckApi.as_view(), name="trucks"),
    path("trucks/<uuid:pk>/", TruckApi.as_view(), name="truck"),

    # driver endpoints
    path("drivers", DriverApi.as_view(), name="drivers"),
    path("drivers/<uuid:pk>/", DriverApi.as_view(), name="driver"),

    # parcel endpoints
    path("parcels", ParcelApi.as_view(), name="parcels"),
    path("parcels/<uuid:pk>/", ParcelApi.as_view(), name="parcel"),

    # shipment endpoints
    path("shipments", ShipmentApi.as_view(), name="shipments"),
    path("shipments/<uuid:pk>/", ShipmentApi.as_view(), name="shipment"),

    # location endpoints
    path("locations", LocationApi.as_view(), name="locations"),

    # analytics endpoints
    path("analytics", AnalyticsApi.as_view(), name="analytics"),
]
