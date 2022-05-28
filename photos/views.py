from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')


def photo_details(request, pk):
    return render(request, 'photo_details.html')


def upload_photo(request):
    return render(request, 'upload_photo.html')  
