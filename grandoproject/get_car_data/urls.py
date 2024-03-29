from django.urls import path
from .views import *

app_name = 'get_car_data'

urlpatterns = [
    path('download/<int:car_id>/', download_car_data, name='download_car_data'),
    path('download/<int:trailer_id>/', download_trailer_data, name='download_trailer_data'),
    path('car/', get_car_data, name='get_car_data'),
    path('trailer/', get_trailer_data, name='get_trailer_data'),
    path('search_car_data/', search_car_field, name='search_car_field'),
    path('search_trailer_data/', search_trailer_field, name='search_trailer_field')

]
