from django.urls import path
from .views import VehicleList, VehicleDetail


app_name = 'api'

urlpatterns = [
    path('', VehicleList.as_view(), name='vehicleList'),
    path('<int:pk>/', VehicleDetail.as_view(), name='vehicleDetail'),
]