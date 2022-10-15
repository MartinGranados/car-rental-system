from django.urls import path
from .views import *


app_name = 'car_rental_system'

urlpatterns = [
    path('', index)
    # path('select/', views.select, name='select'),
    # path('confirm/', views.confirm, name='confirm')
]
