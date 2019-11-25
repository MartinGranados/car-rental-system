from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vehicle

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
        # Still need to figure out how to set a date range and only show vehicles
        # which are available in that date range. May not happen for this project 
        if request.POST['vehicle_type'] == 'any':
            if request.POST['vehicle_class'] == 'any':
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available')}
                else:
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            seats=request.POST['number_of_seats'])}
            else:
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            vehicle_class=request.POST['vehicle_class'])}
                else:
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            vehicle_class=request.POST['vehicle_class'], 
                                                                            seats=request.POST['number_of_seats'])}
        else:
            if request.POST['vehicle_class'] == 'any':
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available',
                                                                            vehicle_type=request.POST['vehicle_type'])}
                else:
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available',
                                                                            vehicle_type=request.POST['vehicle_type'], 
                                                                            seats=request.POST['number_of_seats'])}
            else:
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            vehicle_class=request.POST['vehicle_class'],
                                                                            vehicle_type=request.POST['vehicle_type'])}
                else:
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            vehicle_class=request.POST['vehicle_class'],
                                                                            vehicle_type=request.POST['vehicle_type'], 
                                                                            seats=request.POST['number_of_seats'])}
        # display_filtered = []
        # for item.vehicle_model in filtered_vehicles:
        #     if display_filtered.count(item) == 0:
        #         display_filtered.append(item)
        # single_filtered_vehicles = {'vehicles': display_filtered}
        return render(request, 'reservations/filters.html', filtered_vehicles, {'title': 'Results'})
    # If form has not been filled out yet, show only the form
    return render(request, 'reservations/filters.html')
