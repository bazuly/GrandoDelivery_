from django.urls import path
from .views import *

app_name = 'get_driver_data'

urlpatterns = [
    path('download/<int:driver_id>/', download_driver_data, name='download_driver_data'),
    path('', get_driver_data, name='get_driver_data'),
    path('search_driver/', search_driver_data, name='search_driver_data')
]


