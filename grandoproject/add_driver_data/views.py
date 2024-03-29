from django.shortcuts import render, redirect
from .models import UploadDriverData
from .forms import DriverForm
from django.contrib.auth.decorators import login_required

"""
Добавление данных водителей
"""


@login_required
def add_driver_data(request):
    if request.method == 'POST':
        driver_form = DriverForm(request.POST, request.FILES)
        if driver_form.is_valid():
            driver_data = UploadDriverData()
            driver_data.name = driver_form.cleaned_data['name']
            driver_data.org_name = driver_form.cleaned_data['org_name']
            driver_data.other_data = driver_form.cleaned_data['other_data']
            driver_data.files = request.FILES.get('files')

            driver_data.save()

            print("Data saved successfully")

            return redirect('add_driver_data:add_driver_data')

        else:
            print(driver_form.errors)

    else:
        driver_form = DriverForm()

    return render(request, 'add_driver_data/add_driver_data.html', {'driver_form': driver_form})
