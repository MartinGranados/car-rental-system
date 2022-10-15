from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle, Reservations
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime as dt

def index (request):
    return render(request , 'index.html')
    
# when queryset has duplicate results, return only one of each
def distinct(queryset):
    d = {}
    for item in queryset:
        field_value = getattr(item, "vehicle_model")
        if field_value not in d:
            d[field_value] = item
    return d.values()


def date_validation(request, status_start, status_end):
    rental_length = status_end - status_start
    rental_length_days = int(rental_length.days)
    today = dt.date.today()

    # Ensure end date is after start date
    if rental_length_days < 0:
        raise Exception(
            messages.error(
                request,
                "End date should not be before start date.",
                extra_tags="alert-danger",
            )
        )
    # Ensure days after and including today are chosen
    elif int((today - status_start.date()).days) > 0:
        raise Exception(
            messages.error(
                request,
                "Please choose dates in the present or future.",
                extra_tags="alert-danger",
            )
        )


def filters(request):
    # If form is filled out and submitted, reload the page with the vehicles that
    # match the filters displayed

    if request.method == "POST" and "search_submit" in request.POST:

        # grab start and end dates from form and combine
        status_start = (
            request.POST["status_start_date"] + " " + request.POST["status_start_time"]
        )
        status_start = dt.datetime.strptime(status_start, "%Y-%m-%d %H:%M")

        status_end = (
            request.POST["status_end_date"] + " " + request.POST["status_end_time"]
        )
        status_end = dt.datetime.strptime(status_end, "%Y-%m-%d %H:%M")

        rental_length = status_end - status_start

        # date input validation. return blank form if dates don't validate
        try:
            date_validation(
                request=request, status_start=status_start, status_end=status_end
            )
        except Exception:
            return render(request, "reservations/filters.html")

        # Ensure vehicle is not reserved for the dates supplied
        available_vehicles = Vehicle.objects.exclude(
            reservations__status_start__range=[status_start, status_end]
        )

        available_vehicles = Vehicle.objects.exclude(
            reservations__status_end__range=[status_start, status_end]
        )

        # From available vehicles, apply filters sequentially if needed
        filtered_vehicles = (
            available_vehicles.filter(vehicle_type=request.POST["vehicle_type"])
            if request.POST["vehicle_type"] != "any"
            else available_vehicles
        )
        filtered_vehicles = (
            filtered_vehicles.filter(vehicle_class=request.POST["vehicle_class"])
            if request.POST["vehicle_class"] != "any"
            else filtered_vehicles
        )
        filtered_vehicles = (
            available_vehicles.filter(seats=request.POST["number_of_seats"])
            if request.POST["number_of_seats"] != "any"
            else filtered_vehicles
        )
        filtered_vehicles = {"vehicles": distinct(filtered_vehicles)}

        return render(
            request,
            "reservations/filters.html",
            {
                "vehicles": filtered_vehicles["vehicles"],
                "rental_length": rental_length.days,
                "status_start": status_start,
                "status_end": status_end,
            },
        )
    else:
        # If form has not been filled out yet, show only the form
        return render(request, "reservations/filters.html")


def select(request):
    if request.method == "POST" and "submit_select" in request.POST:
        # view one vehicle in detail
        vehicle = {"vehicles": Vehicle.objects.get(id=request.POST["vehicle_id"])}
        status_start = request.POST["status_start"]
        status_end = request.POST["status_end"]
        return render(
            request,
            "reservations/select.html",
            {
                "vehicles": vehicle["vehicles"],
                "rental_length": request.POST["rental_length"],
                "status_start": status_start,
                "status_end": status_end,
            },
        )


@login_required
def confirm(request):
    if request.method == "POST" and "submit_reserve" in request.POST:
        # add reservation to database using start date, end date and vehicle ID
        rented_vehicle = {
            "vehicles": Vehicle.objects.get(id=request.POST["vehicle_id"])
        }
        vehicle = Vehicle.objects.get(id=request.POST["vehicle_id"])
        print(rented_vehicle)
        print(vehicle)
        status_start = request.POST["status_start"]
        status_end = request.POST["status_end"]
        user = request.user
        reservation = Reservations(
            vehicle=vehicle, status_start=status_start, status_end=status_end, user=user
        )
        reservation.save()
        return render(
            request,
            "reservations/confirm.html",
            {
                "vehicles": vehicle,
                "status_start": status_start,
                "status_end": status_end,
            },
        )

