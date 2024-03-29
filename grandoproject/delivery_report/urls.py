from django.urls import path
from .views import *

app_name = 'delivery_report'


urlpatterns = [
    path('delivery_report_create/', create_delivery_report, name='delivery_report_create'),
    path('delivery_report_history/', delivery_report_history, name='delivery_report_history'),
    path('delivery_report_email/', delivery_report_email, name='delivery_report_email')
]