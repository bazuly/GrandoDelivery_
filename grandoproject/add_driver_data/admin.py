from django.contrib import admin
from .models import UploadDriverData


@admin.register(UploadDriverData)
class UploadDriverDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'other_data']
    search_fields = ['name']
    save_on_top = True



    
    
