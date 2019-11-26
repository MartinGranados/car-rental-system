from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

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

    # Class choices
    economy = 'Economy'
    standard = 'Standard'
    sport = 'Sport'
    luxury = 'Luxury'
    all_classes = 'All'

    VEHICLE_STATUS_CHOICES = [(available,'Available'), (reserved, 'Reserved'), (rented, 'Rented'), (maintenance, 'Maintenance')]
    VEHICLE_TYPE_CHOICES = [(car, 'Car'), (truck, 'Truck'), (van, 'Van'), (suv, 'SUV')]
    VEHICLE_CLASS_CHOICES = [(economy, 'Economy'), (standard, 'Standard'), (sport, 'Sport'), (luxury,'Luxury'), (all_classes, 'All')]

    vehicle_type = models.CharField(max_length = 6, choices = VEHICLE_TYPE_CHOICES, default = car)
    vehicle_class = models.CharField(max_length=9, choices=VEHICLE_CLASS_CHOICES, default=standard)
    vehicle_make = models.CharField(max_length = 14)
    vehicle_model = models.CharField(max_length = 16)
    seats = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(12)])
    price_per_day = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(500.00)])
    vehicle_status = models.CharField(max_length=11, choices=VEHICLE_STATUS_CHOICES, default=available)
    status_start_date = models.DateField()
    status_end_date = models.DateField()
    # reserved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='vehicle_pics')

    def __str__(self):
        return str(self.vehicle_make).title() + ' ' + str(self.vehicle_model).title() # + ' Seat ' + self.vehicle_type.title()