from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from reservations.models import Reservations, Vehicle
import datetime


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You may now sign in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    reservations = Reservations.objects.filter(user=request.user)
    future_reservations = reservations.filter(
        status_start__gte=datetime.date.today()
    )
    past_reservations = reservations.filter(
        status_end__lte=datetime.date.today()
    )
    reservations = {"future_reservations": future_reservations, "past_reservations": past_reservations}

    return render(request, 'users/profile.html', reservations)
