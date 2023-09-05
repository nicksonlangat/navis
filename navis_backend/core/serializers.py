from rest_framework import serializers
from accounts.serializers import UserOutputSerializer
from .models import Location, Client, Parcel, Truck, Driver, Shipment

class LocationSerializer(serializers.ModelSerializer):
        class Meta:
            model = Location
            fields = ["id", "name"]

class ClientSerializer(serializers.ModelSerializer):
        class Meta:
            model = Client
            fields = [
                "id", "first_name", "last_name",
                "email", "created_at", "updated_at",
                "phone_number", "location", "identity_number"
                ]
        
        def to_representation(self, instance):
            data = super(ClientSerializer, self).to_representation(instance)
            try:
                data["location"] = LocationSerializer(Location.objects.get(name=instance.location.name)).data
            except AttributeError:
                 data["location"] = LocationSerializer(Location.objects.get(name=instance["location"].name)).data
            return data

            

class ParcelSerializer(serializers.ModelSerializer):
        class Meta:
            model = Parcel
            fields = [
                "id", "client", "weight", "item", 
                "destination", "recipient_contact", 
                "status", "parcel_number", "created_at",
                "updated_at"
                ]

        def to_representation(self, instance):
            data = super(ParcelSerializer, self).to_representation(instance)
            data["client"] = UserOutputSerializer(instance.client).data if instance.client else None
            data["destination"] = LocationSerializer(Location.objects.get(name=instance.destination)).data
            return data


class TruckSerializer(serializers.ModelSerializer):
        class Meta:
            model = Truck
            fields = [
                "id", "manufacturer", "model", 
                "chasis_number", "created_at", "carry_weight",
                "registration_number", "engine_size", 
                "engine_power", "yom", "updated_at"
                ]


class DriverSerializer(serializers.ModelSerializer):
        class Meta:
            model = Driver
            fields = [
                "id", "first_name", "last_name", 
                "email", "phone_number", "created_at",
                "licence_number", "identity_number", 
                "kra_pin", "updated_at"
                ]



class ShipmentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Shipment
            fields = [
                "id", "truck", "driver",
                "parcels", "shipment_number", 
                "status", "route_from", "created_at",
                "updated_at", "route_to", "departure_date",
                "arrival_date", "parcels"
                ]
        
        def to_representation(self, instance):
            data = super(ShipmentSerializer, self).to_representation(instance)
            data["truck"] = TruckSerializer(Truck.objects.get(id=instance.truck.id)).data
            data["driver"] = DriverSerializer(Driver.objects.get(id=instance.driver.id)).data
            data["route_from"] = LocationSerializer(Location.objects.get(id=instance.route_from.id)).data
            data["route_to"] = LocationSerializer(Location.objects.get(id=instance.route_to.id)).data
            data["parcels"] = ParcelSerializer(instance.parcels.all(), many=True).data
            return data
