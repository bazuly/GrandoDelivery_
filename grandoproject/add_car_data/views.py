from django.shortcuts import render, redirect
from .models import UploadCarData, UploadTrailerData
from .forms import CarForm, TrailerForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

"""
Добавление данных на транспортное средство
"""


@login_required
def add_car_data(request):
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES, prefix='car')
        if car_form.is_valid():
            car_data = UploadCarData(
                car_name=car_form.cleaned_data['car_name'],
                car_number=car_form.cleaned_data['car_number'],
                tonnage=car_form.cleaned_data['tonnage'],
                capacity=car_form.cleaned_data['capacity'],
                car_scan_doc=request.FILES.get('car_scan_doc')
            )

            car_data.save()

            print('car data saved successfully')

            return HttpResponseRedirect(reverse('add_car_data:add_car_data'))
        else:
            print('Form is not valid', car_form.errors)

    else:
        car_form = CarForm(prefix='car')

    return render(request, 'add_car_data/add_car_data.html', {'car_form': car_form})


"""
Добавление данных полуприцепов
"""


@login_required
def add_trailer_data(request):
    if request.method == 'POST':
        trailer_form = TrailerForm(request.POST, request.FILES, prefix='trailer')
        if trailer_form.is_valid():
            trailer_data = UploadTrailerData(
                trailer_name=trailer_form.cleaned_data['trailer_name'],
                trailer_number=trailer_form.cleaned_data['trailer_number'],
                trailer_scan_doc=request.FILES.get('trailer_scan_doc')
            )
            trailer_data.save()

            print('trailer data saved successfully')

            return HttpResponseRedirect(reverse('add_car_data:add_trailer_data'))
        else:
            print('Form is not valid', trailer_form.errors)
    else:
        trailer_form = TrailerForm(prefix='trailer')

    return render(request, 'add_car_data/add_trailer_data.html', {'trailer_form': trailer_form})
