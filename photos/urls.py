from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<str:pk>/', views.photo_details, name='details'),
    path('upload/', views.upload_photo, name='upload'), 
]