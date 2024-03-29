from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from add_driver_data.models import UploadDriverData
from django.http import FileResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

"""
Получение данных водителей
Весь список
"""


@login_required
def get_driver_data(request):
    driver_data = UploadDriverData.objects.all()

    # pagination
    for data in driver_data:
        data.has_file = data.has_file()
    items_per_page = 1
    paginator = Paginator(driver_data, items_per_page)
    page = request.GET.get('page')
    try:
        driver_data = paginator.page(page)
    except PageNotAnInteger:
        driver_data = paginator.page(1)
    except EmptyPage:
        driver_data = paginator.page(paginator.num_pages)

    context = {
        'driver_data': driver_data
    }

    return render(request, 'get_driver_data/get_driver_data.html', context)


@login_required
def download_driver_data(request, driver_id):
    driver_data = get_object_or_404(UploadDriverData, pk=driver_id)
    file_path = driver_data.files.path
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    return response


@login_required
def search_driver_data(request):
    query = request.GET.get('q')
    query_lower = query.lower()
    driver_data = UploadDriverData.objects.all()

    if query:
        driver_data = UploadDriverData.objects.filter(
            Q(name__icontains=query_lower) |
            Q(org_name__icontains=query_lower)
        )
    else:
        query = driver_data

    context = {
        'driver_data': driver_data,
        'query': query
    }

    return render(request, 'get_driver_data/get_driver_data.html', context)
