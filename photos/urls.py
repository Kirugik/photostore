from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('details/<str:pk>/', views.photo_details, name='details'),
    path('upload/', views.upload_photo, name='upload'), 
    path('search/', views.search_categories, name='search_categories')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)