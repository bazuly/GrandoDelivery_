from django.contrib import admin
from django.urls import path, include
from grandoproject import settings
from django.conf.urls.static import static
from .views import home_page

urlpatterns = [
    path('home_page/', home_page, name='home_page'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('add_driver_data/', include('add_driver_data.urls',
                                     namespace='add_driver_data')),
    path('get_driver_data/', include('get_driver_data.urls',
                                     namespace='get_driver_data')),
    path('add_car_data/', include('add_car_data.urls', namespace='add_car_data')),
    path('get_car_data/', include('get_car_data.urls', namespace='get_car_data')),
    path('manager_client/', include('manager_client.urls', namespace='manager_client')),
    path('delivery_report/', include('delivery_report.urls',
                                     namespace='delivery_report')),
    # path("", include('grando_blog.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
