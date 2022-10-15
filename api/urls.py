from django.urls import path
from .views import VehicleList, VehicleDetail


app_name = 'api'

urlpatterns = [
    path('<int:pk>/', VehicleDetail.as_view(), name='vehicleDetail'),
    path('', VehicleList.as_view(), name='vehicleList'),
]