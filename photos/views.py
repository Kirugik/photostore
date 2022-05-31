from django.shortcuts import render, redirect
from .models import Category, Location, Image

# Create your views here.
def index(request):
    category = request.GET.get('category')
    
    if category == None:
        images = Image.objects.all()
    else:
        images = Image.objects.filter(category__name=category)
    categories = Category.objects.all() 


    location = request.GET.get('location') 
    if location == None:
        # locations = Location.objects.all()  
        loc_images = Image.objects.all()
    else:
        # locations = Location.objects.filter(location__name=location) 
        loc_images = Image.objects.filter(location__name=location) 
    locations = Location.objects.all()  

    context = {'categories':categories, 'images':images, 'locations':locations, 'loc_images':loc_images}
    return render(request, 'index.html', context)




def photo_details(request, pk):
    photo = Image.objects.get(id=pk)
    return render(request, 'photo_details.html', {'photo':photo}) 



def upload_photo(request):
    categories = Category.objects.all()
    
    if request.method == "POST":
        data = request.POST
        image = request.FILES.get("image") 

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new']) 
        else:
            category = None

        photo = Image.objects.create(category=category, description=data['description'], image=image)

        return redirect('index') 

    context = {'categories':categories}
    return render(request, 'upload_photo.html', context)  


# def search_categories(request): 

#     if 'image' in request.GET and request.GET["image"]:
#         search_term = request.GET.get("image")
#         searched_photos = Image.search_image(search_term)
#         message = f"{search_term}"

#         return render(request, 'all-news/search.html',{"message":message,"articles": searched_photos})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',{"message":message})
