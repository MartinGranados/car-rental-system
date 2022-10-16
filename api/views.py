from rest_framework import generics
from car_rental_system.models import Vehicle, Reservations
from .serializers import ReservationSerializer, VehicleSerializer



class VehicleList(generics.ListAPIView):
    model = Vehicle
    serializer_class = VehicleSerializer
    
    def get_queryset(self):
        queryset = Vehicle.objects.all()
        vehicle_type = self.request.query_params['vehicleType']
        # vehicle_class = self.request.query_params['vehicleClass']
        # seats = self.request.query_params['seats']

        if vehicle_type is not None:
            queryset = queryset.filter(vehicle_type=vehicle_type)
    
        return queryset


class VehicleDetail(generics.RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    pass


class ReservationDetail(generics.RetrieveAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationSerializer
    pass


