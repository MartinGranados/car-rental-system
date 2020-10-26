from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vehicle
from django.contrib import messages
import datetime as dt

def distinct(queryset, fieldname):
    d = {}
    for item in queryset:
        field_value = getattr(item, fieldname)
        if field_value not in d:
            d[field_value] = item
    return d.values()


def filters(request):
    # If form is filled out and submitted, reload the page with the vehicles that
    # match the filters displayed

    if request.method == 'POST':
        print(request.POST['status_start_time'])
        status_start = request.POST['status_start_date']
        status_start = status_start + ' ' + request.POST['status_start_time']
        print('**********' + status_start + '**********')
        status_end = request.POST['status_end_date']
        status_start = dt.datetime.strptime(status_start, '%Y-%m-%d %H:%M')
        status_end = dt.datetime.strptime(status_end, '%Y-%m-%d')
        rental_length = int(str(status_end.date() - status_start.date()).split(' ')[0])

        # date input validation
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
                                                                            status_end_date__gte=status_end.date())
                                                                            .order_by('vehicle_model')}
                    print(filtered_vehicles)
                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)
                else:
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            seats=request.POST['number_of_seats'],
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())
                                                                            .order_by('vehicle_model')}
                                                                            
                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)
            else:
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            vehicle_class=request.POST['vehicle_class'],
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())
                                                                            .order_by('vehicle_model')}

                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)
                else:
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            vehicle_class=request.POST['vehicle_class'], 
                                                                            seats=request.POST['number_of_seats'],
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())
                                                                            .order_by('vehicle_model')}
                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)                
        else:
            if request.POST['vehicle_class'] == 'any':
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available',
                                                                            vehicle_type=request.POST['vehicle_type'],
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())
                                                                            .order_by('vehicle_model')}
                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)
                else:
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available',
                                                                            vehicle_type=request.POST['vehicle_type'], 
                                                                            seats=request.POST['number_of_seats'],
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())
                                                                            .order_by('vehicle_model')}
                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)
            else:
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            vehicle_class=request.POST['vehicle_class'],
                                                                            vehicle_type=request.POST['vehicle_type'],
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())
                                                                            .order_by('vehicle_model')}
                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)
                else:
                    filtered_vehicles = {'vehicles': Vehicle.objects.filter(vehicle_status='Available', 
                                                                            vehicle_class=request.POST['vehicle_class'],
                                                                            vehicle_type=request.POST['vehicle_type'], 
                                                                            seats=request.POST['number_of_seats'],
                                                                            status_start_date__lte=status_start.date(),
                                                                            status_end_date__gte=status_end.date())
                                                                            .order_by('vehicle_model')}
                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)

        print(rental_length)
        return render(request, 'reservations/filters.html', filtered_vehicles, rental_length)
    else:
        # If form has not been filled out yet, show only the form
        return render(request, 'reservations/filters.html')

# def confirm(request):
    


