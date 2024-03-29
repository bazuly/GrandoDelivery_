from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from add_car_data.models import UploadCarData, UploadTrailerData
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""
Получение данных на транспортное средство
"""


@login_required
def get_car_data(request):
    car_data = UploadCarData.objects.all()

    for data in car_data:
        data.has_file = data.has_file()
    
    items_per_page = 5
    paginator = Paginator(car_data, items_per_page)
    
    page = request.GET.get('page')
    try:
        car_data = paginator.page(page)
        
    except PageNotAnInteger:
        car_data = paginator.page(1)
        
    except EmptyPage:
        car_data = paginator.page(paginator.num_pages)

    context = {
        'car_data': car_data
        }

    return render(request, 'get_car_data/get_car_data.html', context)


@login_required
def download_car_data(request, car_id):
    car_data = get_object_or_404(UploadCarData, pk=car_id)
    file_path = car_data.car_scan_doc.path
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    return response


@login_required
def get_trailer_data(request):
    trailer_data = UploadTrailerData.objects.all()

    for data in trailer_data:
        data.has_file = data.has_file()

    items_per_page = 5
    paginator = Paginator(trailer_data, items_per_page)
    page = request.GET.get('page')
    try:
        trailer_data = paginator.page(page)
    except PageNotAnInteger:
        trailer_data = paginator.page(1)
    except EmptyPage:
        trailer_data = paginator.page(paginator.num_pages)
    context = {
        'trailer_data': trailer_data
        }

    return render(request, 'get_car_data/get_trailer_data.html', context)


@login_required
def download_trailer_data(request, trailer_id):
    trailer_data = get_object_or_404(UploadTrailerData, pk=trailer_id)
    file_path = trailer_data.trailer_scan_doc.path
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    return response


# Говно, переделать
@login_required
def search_car_field(request):
    car_data = UploadCarData.objects.all()
    query = request.GET.get('q')
    if query:
        car_data = UploadCarData.objects.filter(
            Q(car_number__icontains=query)     
        )
    else:
        query = UploadCarData.objects.all()
    context = {
        'car_data': car_data,
        'query': query
    }
    
    return render(request, 'get_car_data/get_car_data.html', context)


@login_required
def search_trailer_field(request):
    query = request.GET.get('q')
    trailer_data = UploadTrailerData.objects.all()
    if query:
        trailer_data = UploadTrailerData.objects.filter(
            Q(trailer_number__icontains=query)     
        )
    else:
        query = UploadTrailerData.objects.all()

    context = {
        'trailer_data': trailer_data,
        'query': query
    }
    
    return render(request, 'get_car_data/get_trailer_data.html', context)
