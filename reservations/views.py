from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle


def home(request):
    available_vehicles = {
        'vehicles': Vehicle.objects.filter(vehicle_status = 'Available')
    }
    return render(request, 'reservations/home.html', available_vehicles, {'title': 'About'})

def filters(request):
    return render(request, 'reservations/filters.html')
