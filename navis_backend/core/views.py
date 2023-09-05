from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView, ListAPIView, 
    RetrieveUpdateAPIView, 
    RetrieveDestroyAPIView
)

from common.pagination import (
    LimitOffsetPagination,
    get_paginated_response,
)
from core.selectors import (
    client_list, parcel_list, 
    truck_list, driver_list, 
    location_list, shipment_list
)
from .services import (
    client_create, client_update,
    truck_create, truck_update,
    driver_create, driver_update,
    parcel_create, parcel_update,
    shipment_create, shipment_update

)
from .models import (
    Client, Parcel, 
    Truck, Driver, Shipment
)
from .serializers import (
    ClientSerializer, ParcelSerializer, 
    TruckSerializer, DriverSerializer,
    LocationSerializer, ShipmentSerializer
)

class ClientApi(
    CreateAPIView, ListAPIView, 
    RetrieveUpdateAPIView, RetrieveDestroyAPIView):

    serializer_class = ClientSerializer

    class Pagination(LimitOffsetPagination):
        default_limit = 25

    queryset = client_list()

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        new_client = client_create(**serializer.validated_data)
        return Response({"data": ClientSerializer(new_client).data}, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        filters = request.query_params
        qs = client_list(filters=filters)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=qs,
            request=request,
            view=self,
        )

    def patch(self, request, pk, format=None):  
        client = Client.objects.get(id=pk)
        serializer = self.serializer_class(client, data=request.data)
        if serializer.is_valid():
            client_update(client, data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        client = Client.objects.get(id=pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TruckApi(
    CreateAPIView, ListAPIView, 
    RetrieveUpdateAPIView, RetrieveDestroyAPIView):

    serializer_class = TruckSerializer

    class Pagination(LimitOffsetPagination):
        default_limit = 25

    queryset = truck_list()

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        truck_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        filters = request.query_params
        qs = truck_list(filters=filters)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=qs,
            request=request,
            view=self,
        )

    def patch(self, request, pk, format=None):  
        truck = Truck.objects.get(id=pk)
        serializer = self.serializer_class(truck, data=request.data)
        if serializer.is_valid():
            truck_update(truck, data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        truck = Truck.objects.get(id=pk)
        truck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DriverApi(
    CreateAPIView, ListAPIView, 
    RetrieveUpdateAPIView, RetrieveDestroyAPIView):

    serializer_class = DriverSerializer

    class Pagination(LimitOffsetPagination):
        default_limit = 25

    queryset = driver_list()

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        driver_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        filters = request.query_params
        qs = driver_list(filters=filters)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=qs,
            request=request,
            view=self,
        )

    def patch(self, request, pk, format=None):  
        driver = Driver.objects.get(id=pk)
        serializer = self.serializer_class(driver, data=request.data)
        if serializer.is_valid():
            driver_update(driver, data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        driver = Driver.objects.get(id=pk)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ParcelApi(
    CreateAPIView, ListAPIView, 
    RetrieveUpdateAPIView, RetrieveDestroyAPIView):

    serializer_class = ParcelSerializer

    class Pagination(LimitOffsetPagination):
        default_limit = 25

    queryset = parcel_list()

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        parcel_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        filters = request.query_params
        qs = parcel_list(filters=filters)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=qs,
            request=request,
            view=self,
        )

    def patch(self, request, pk, format=None):  
        parcel = Parcel.objects.get(id=pk)
        serializer = self.serializer_class(parcel, data=request.data)
        if serializer.is_valid():
            parcel_update(parcel, data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        parcel = Parcel.objects.get(id=pk)
        parcel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShipmentApi(
    CreateAPIView, ListAPIView, 
    RetrieveUpdateAPIView, RetrieveDestroyAPIView):

    serializer_class = ShipmentSerializer

    class Pagination(LimitOffsetPagination):
        default_limit = 25

    queryset = shipment_list()

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.pop("parcels")
        shipment_create(**serializer.validated_data)
        return Response( status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        filters = request.query_params
        qs = shipment_list(filters=filters)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=qs,
            request=request,
            view=self,
        )

    def patch(self, request, pk, format=None):  
        shipment = Shipment.objects.get(id=pk)
        serializer = self.serializer_class(shipment, data=request.data)
        if serializer.is_valid():
            shipment_update(shipment, data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        shipment = Shipment.objects.get(id=pk)
        shipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LocationApi(ListAPIView):

    serializer_class = LocationSerializer

    class Pagination(LimitOffsetPagination):
        default_limit = 25

    queryset = location_list()

    def get(self, request, *args, **kwargs):
        filters = request.query_params
        qs = location_list(filters=filters)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=qs,
            request=request,
            view=self,
        )