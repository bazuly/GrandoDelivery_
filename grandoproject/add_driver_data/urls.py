from django.urls import path
from . import views

app_name = 'add_driver_data'


urlpatterns = [
    path('', views.add_driver_data, name='add_driver_data'),
]
