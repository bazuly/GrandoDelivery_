from django.contrib import admin
from .models import Client, Manager

admin.site.register(Client)
admin.site.register(Manager)


class Client(admin.ModelAdmin):
    list_display = ['name', 'contacts', ]
    save_on_top = True


class Manager(admin.ModelAdmin):
    list_display = ['name']
    save_on_top = True
