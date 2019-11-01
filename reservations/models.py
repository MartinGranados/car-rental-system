from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    # Car choices
    car = 'car'
    truck = 'truck'
    van = 'van'
    suv = 'SUV'

    # Status choices
    available = 'Available'
    reserved = 'Reserved'
    rented = 'Rented'
    maintenance = 'Maintenance'


    VEHICLE_STATUS_CHOICES = [(available,'Available'), (reserved, 'Reserved'), (rented, 'Rented'), (maintenance, 'Maintenance')]
    vehicle_type_choices = [(car, 'Car'), (truck, 'Truck'), (van, 'Van'), (suv, 'SUV')]
    vehicle_type = models.CharField(max_length = 6, choices = vehicle_type_choices, default = car)
    seats = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=5, decimal_places=2)
    vehicle_status = models.CharField(max_length=11, choices=VEHICLE_STATUS_CHOICES, default=available)
    reserved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='vehicle_pics')

    def __str__(self):
        return str(self.seats) + ' Seat ' + self.vehicle_type.title()