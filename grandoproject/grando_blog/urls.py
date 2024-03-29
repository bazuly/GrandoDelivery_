from django.urls import path
from . import views

app_name = 'grando_blog'

urlpatterns = [
    path("", views.blog_index, name="main_blog"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
]
