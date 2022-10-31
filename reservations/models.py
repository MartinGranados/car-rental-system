from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Vehicle(models.Model):

    VEHICLE_STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('rented', 'Rented'),
        ('maintenance', 'Maintenance')
    ]
    VEHICLE_TYPE_CHOICES = [
        ('car', 'Car'),
        ('truck', 'Truck'),
        ('van', 'Van'),
        ('suv', 'SUV')
    ]
    VEHICLE_CLASS_CHOICES = [
        ('economy', 'Economy'),
        ('standard', 'Standard'),
        ('sport', 'Sport'),
        ('luxury', 'Luxury')
    ]

    vehicle_type = models.CharField(max_length=6, choices=VEHICLE_TYPE_CHOICES, default='car')
    vehicle_class = models.CharField(max_length=9, choices=VEHICLE_CLASS_CHOICES, default='standard')
    vehicle_make = models.CharField(max_length=14)
    vehicle_model = models.CharField(max_length=16)
    seats = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(12)])
    price_per_day = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(500.00)])
    image = models.ImageField(default='default.jpg', upload_to='vehicle_pics')

    def __str__(self):
        return str(self.vehicle_make) + ' ' + str(self.vehicle_model)


class Reservations(models.Model):

    VEHICLE_STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('rented', 'Rented'),
        ('maintenance', 'Maintenance')
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    # status = models.CharField(max_length=11, choices=VEHICLE_STATUS_CHOICES, default='available')
    status_start = models.DateTimeField(null=True, blank=True)
    status_end = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vehicle) + ',' + str(self.status_start) + ',' + str(self.status_end)
