from rest_framework import generics
from car_rental_system.models import Vehicle, Reservations
from .serializers import ReservationSerializer, VehicleSerializer

class VehicleList(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    pass

class VehicleDetail(generics.RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    pass

class ReservationDetail(generics.RetrieveAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationSerializer
