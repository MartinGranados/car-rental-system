from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle, Reservations
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

    if request.method == 'POST' and 'search_submit' in request.POST:

        status_start = request.POST['status_start_date']
        status_start = status_start + ' ' + request.POST['status_start_time']
        status_start = dt.datetime.strptime(status_start, '%Y-%m-%d %H:%M')

        status_end = request.POST['status_end_date']
        status_end = status_end + ' ' + request.POST['status_end_time']
        status_end = dt.datetime.strptime(status_end, '%Y-%m-%d %H:%M')

        rental_length = (status_end - status_start)
        print(str(rental_length))

        # date input validation
        if 'days' in str(rental_length):
            rental_length_days = int(str(rental_length)[0:2].strip(' '))

            if rental_length_days > 14 or rental_length_days < 0 or (int(str((dt.date.today()) - status_start.date()).split(' ')[0])) > 0:

                if rental_length > 14:
                    messages.error(request, 'Please contact us to reserve a vehicle for longer than 14 days.', extra_tags='alert-danger')
                    return render(request, 'reservations/filters.html')
                #
                elif rental_length < 0:
                    messages.error(request, 'End date should not be before start date.', extra_tags='alert-danger')
                    return render(request, 'reservations/filters.html')
                # Ensure days after and including today are chosen
                elif (int(str((dt.date.today()) - status_start.date()).split(' ')[0])) > 0:
                    messages.error(request, 'Please choose dates in the present or future.', extra_tags='alert-danger')
                    return render(request, 'reservations/filters.html')

        # Ensure vehicle is not reserved for the dates supplied
        available_vehicles = Vehicle.objects.exclude(reservations__status_start__range=[status_start, status_end])
        if request.POST['vehicle_type'] == 'any':
            if request.POST['vehicle_class'] == 'any':

                # Any type, class and number of seats
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {
                        'vehicles': available_vehicles.all().order_by('vehicle_model')
                    }

                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}

                # Filtered by # of seats
                else:
                    filtered_vehicles = {
                        'vehicles': available_vehicles.filter(seats=request.POST['number_of_seats'])
                        .order_by('vehicle_model')
                    }

                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)

            else:
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {
                        'vehicles': available_vehicles.filter(
                            vehicle_class=request.POST['vehicle_class']
                        ).order_by('vehicle_model')
                    }

                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)
                else:
                    filtered_vehicles = {
                        'vehicles': available_vehicles.filter(
                            vehicle_class=request.POST['vehicle_class'],
                            seats=request.POST['number_of_seats']
                        ).order_by('vehicle_model')
                    }
                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)
        else:
            if request.POST['vehicle_class'] == 'any':
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {
                        'vehicles': available_vehicles.filter(
                            vehicle_type=request.POST['vehicle_type']
                        ).order_by('vehicle_model')
                    }
                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)
                else:
                    filtered_vehicles = {'vehicles': available_vehicles.filter(vehicle_type=request.POST['vehicle_type'],
                                                                               seats=request.POST['number_of_seats'])
                                                                               .order_by('vehicle_model')}
                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)
            else:
                if request.POST['number_of_seats'] == 'any':
                    filtered_vehicles = {'vehicles': available_vehicles.filter(vehicle_class=request.POST['vehicle_class'],
                                                                            vehicle_type=request.POST['vehicle_type'])
                                                                            .order_by('vehicle_model')}
                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)
                else:
                    filtered_vehicles = {'vehicles': available_vehicles.filter(vehicle_class=request.POST['vehicle_class'],
                                                                               vehicle_type=request.POST['vehicle_type'], 
                                                                               seats=request.POST['number_of_seats'])
                                                                               .order_by('vehicle_model')}
                    filtered_vehicles = {'vehicles': distinct(filtered_vehicles['vehicles'], 'vehicle_model')}
                    print(filtered_vehicles)

        print(status_start)
        return render(request, 'reservations/filters.html', {'vehicles': filtered_vehicles['vehicles'], 'rental_length': rental_length, 'status_start': status_start, 'status_end': status_end})

    elif request.method == 'POST' and 'submit_select' in request.POST:
        # view one vehicle in detail
        vehicle = {'vehicles': Vehicle.objects.get(id=request.POST['vehicle_id'])}
        status_start = request.POST['status_start']
        status_end = request.POST['status_end']
        return render(
            request, 'reservations/filtered.html',
            {
                'vehicles': vehicle['vehicles'],
                'rental_length': request.POST['rental_length'],
                'status_start': status_start,
                'status_end': status_end
            }
        )

    elif request.method == 'POST' and 'submit_reserve' in request.POST:
        # add reservation to database using start date, end date and vehicle ID
        vehicle = Vehicle.objects.get(id=request.POST['vehicle_id'])
        status_start = request.POST['status_start']
        status_end = request.POST['status_end']
        reservation = Reservations(vehicle = vehicle, status_start = status_start, status_end = status_end)
        reservation.save()
        return render(request, 'reservations/filters.html')


    else:
        # If form has not been filled out yet, show only the form
        return render(request, 'reservations/filters.html')

    
