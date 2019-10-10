from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle


def home(request):
    context = {
        'vehicles': Vehicle.objects.filter(available=True)
    }
    return render(request, 'reservations/home.html', context, {'title': 'About'})
