from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vehicle
import datetime as dt

#####################
# Removing for now, may be unnecessary
# def home(request):
#     available_vehicles = {
#         'vehicles': Vehicle.objects.filter(vehicle_type = 'car')
#     }
#     return render(request, 'reservations/home.html', available_vehicles, {'title': 'About'})
#####################

def filters(request):
    # If form is filled out and submitted, reload the page with the vehicles that
    # match the filters displayed
    if request.method == 'POST':
        status_start = request.POST['status_start_date']
        status_end = request.POST['status_end_date']

        status_start = dt.datetime.strptime(status_start, '%Y-%m-%d')
        status_end = dt.datetime.strptime(status_end, '%Y-%m-%d')
        
        if request.POST['vehicle_type'] == 'any':
            if request.POST['vehicle_class'] == 'any':
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available',
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())}
                else:
                    # filtered_vehicles = {'vehicles': Vehicle.objects.filter(seats=request.POST['number_of_seats'])}
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            seats=request.POST['number_of_seats'],
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())}
            else:
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            vehicle_class=request.POST['vehicle_class'],
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())}
                else:
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            vehicle_class=request.POST['vehicle_class'], 
                                                                            seats=request.POST['number_of_seats'],
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())}
        else:
            if request.POST['vehicle_class'] == 'any':
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available',
                                                                            vehicle_type=request.POST['vehicle_type'],
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())}
                else:
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available',
                                                                            vehicle_type=request.POST['vehicle_type'], 
                                                                            seats=request.POST['number_of_seats'],
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())}
            else:
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            vehicle_class=request.POST['vehicle_class'],
                                                                            vehicle_type=request.POST['vehicle_type'],
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())}
                else:
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            vehicle_class=request.POST['vehicle_class'],
                                                                            vehicle_type=request.POST['vehicle_type'], 
                                                                            seats=request.POST['number_of_seats'],
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())}
            
        
        return render(request, 'reservations/filters.html', filtered_vehicles, {'title': 'Results'})
    # If form has not been filled out yet, show only the form
    return render(request, 'reservations/filters.html')
