from django.db import transaction
from common.services import model_update
from .models import Client, Truck, Driver, Parcel, Shipment

@transaction.atomic
def truck_create(*, 
                  manufacturer, model, chasis_number, 
                  carry_weight, registration_number,
                    engine_size, engine_power, yom) -> Truck:
    obj = Truck(
        manufacturer=manufacturer,
        model=model,
        chasis_number=chasis_number,
        carry_weight=carry_weight,
        registration_number=registration_number,
        engine_size=engine_size,
        engine_power=engine_power,
        yom=yom
    )

    obj.full_clean()
    obj.save()

    return obj


@transaction.atomic
def truck_update(*, truck: Truck, data) -> Truck:
    non_side_effect_fields = []

    truck, has_updated = model_update(instance=truck, fields=non_side_effect_fields, data=data)

    return truck

@transaction.atomic
def client_create(*, first_name, last_name, email, phone_number, identity_number, location) -> Client:
    obj = Client(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        identity_number=identity_number,
        location=location
    )

    obj.full_clean()
    obj.save()

    return obj


@transaction.atomic
def client_update(*, client: Client, data) -> Client:
    non_side_effect_fields = []

    client, has_updated = model_update(instance=client, fields=non_side_effect_fields, data=data)

    return client


@transaction.atomic
def driver_create(*, 
                  first_name, last_name, email, 
                  phone_number, identity_number, 
                  licence_number, kra_pin) -> Driver:
    obj = Driver(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        identity_number=identity_number,
        licence_number=licence_number,
        kra_pin=kra_pin
    )

    obj.full_clean()
    obj.save()

    return obj


@transaction.atomic
def driver_update(*, driver: Driver, data) -> Driver:
    non_side_effect_fields = []

    driver, has_updated = model_update(instance=driver, fields=non_side_effect_fields, data=data)

    return driver


@transaction.atomic
def parcel_create(*, 
                  client, weight, 
                  item, status, destination,
                  recipient_contact, **kwargs) -> Parcel:
    obj = Parcel(
        client=client,
        weight=weight,
        status=status,
        item=item,
        destination=destination,
        recipient_contact=recipient_contact
    )

    obj.full_clean()
    obj.save()

    return obj


@transaction.atomic
def parcel_update(*, parcel: Parcel, data) -> Parcel:
    non_side_effect_fields = []

    parcel, has_updated = model_update(instance=parcel, fields=non_side_effect_fields, data=data)

    return parcel


@transaction.atomic
def shipment_create(*, 
                  truck, driver, 
                  status, route_from,
                  route_to, departure_date,
                  arrival_date) -> Shipment:
    obj = Shipment(
       truck=truck,
       driver=driver,
       status=status,
       route_from=route_from,
       route_to=route_to,
       departure_date=departure_date,
       arrival_date=arrival_date
    )

    obj.full_clean()
    obj.save()

    return obj


@transaction.atomic
def shipment_update(*, shipment: Shipment, data) -> Shipment:
    non_side_effect_fields = []

    shipment, has_updated = model_update(instance=shipment, fields=non_side_effect_fields, data=data)

    return shipment
