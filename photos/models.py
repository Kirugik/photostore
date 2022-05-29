from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(image=value)





class Location(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
    
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)


        


class Image(models.Model):
    image = models.ImageField(upload_to='photos/', null=False, blank=False) 
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True) 

    def __str__(self):
        return self.name 
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete() 
    
    @classmethod 
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image

    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(category__name=category) 
        return images
    
    @classmethod  
    def filter_by_location(cls, location):
        location_taken = Image.objects.filter(location_taken=location).all()
        return location_taken
    
    class Meta:
        ordering = ['pub_date']






