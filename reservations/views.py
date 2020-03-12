from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vehicle
from django.contrib import messages
import datetime as dt

def filters(request):
    # If form is filled out and submitted, reload the page with the vehicles that
    # match the filters displayed

    if request.method == 'POST':
        status_start = request.POST['status_start_date']
        status_end = request.POST['status_end_date']
        status_start = dt.datetime.strptime(status_start, '%Y-%m-%d')
        status_end = dt.datetime.strptime(status_end, '%Y-%m-%d')
        rental_length = int(str(status_end.date() - status_start.date()).split(' ')[0]) #{'rental_length': int(str(status_end.date() - status_start.date()).split(' ')[0])}
        print(status_start.date(), dt.date.today(), status_end, '***', str(((dt.date.today()) - status_start.date())), '***')

        if rental_length > 14 or rental_length < 0 or (int(str((dt.date.today()) - status_start.date()).split(' ')[0])) > 0:
            if rental_length > 14:
                messages.error(request,'Please contact us to reserve a vehicle for longer than 14 days.', extra_tags='alert-danger')
                return render(request, 'reservations/filters.html')
            #
            elif rental_length < 0:
                messages.error(request,'End date should not be before start date.', extra_tags='alert-danger')
                return render(request, 'reservations/filters.html')
            # Ensure days after and including today are chosen
            elif (int(str((dt.date.today()) - status_start.date()).split(' ')[0])) > 0:
                messages.error(request,'Please choose dates in the present or future.', extra_tags='alert-danger')
                return render(request, 'reservations/filters.html')

        
        if request.POST['vehicle_type'] == 'any':
            if request.POST['vehicle_class'] == 'any':
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available',
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())}
                else:
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
            
        
        return render(request, 'reservations/filters.html', filtered_vehicles)
    else:
        # If form has not been filled out yet, show only the form
        return render(request, 'reservations/filters.html')

# def confirm(request):
    


