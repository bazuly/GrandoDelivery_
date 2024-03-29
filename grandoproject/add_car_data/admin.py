from django.contrib import admin
from .models import UploadCarData, UploadTrailerData

@admin.register(UploadCarData)
class UploadCarDataAdmin(admin.ModelAdmin):
    list_display = ['car_name', 'car_number']
    search_fields = ['car_name', 'car_number']
    
    
@admin.register(UploadTrailerData)
class UploadTrailerDataAdmin(admin.ModelAdmin):
    list_display = ['trailer_name', 'trailer_number']
    search_fields = ['trailer_name', 'trailer_number']
    
    