from django.test import TestCase

from .models import Category, Location, Image

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.travelling = Category(name='Travel')
        self.travelling.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.travelling, Category))

    def test_save_category(self):
        self.travelling.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.travelling.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)   


class TestLocation(TestCase):
    def setUp(self):
        self.nairobi = Location(name='Nairobi')
        self.nairobi.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi, Location))

    def test_save_location(self):
        self.nairobi.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_get_locations(self):
        self.nairobi.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 1)
    
    def test_delete_location(self): 
        self.nairobi.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update_location(self):
        new_location = 'Nakuru'
        self.nairobi.update_location(self.nairobi.id, new_location)
        changed_location = Location.objects.filter(name='Nakuru')
        self.assertTrue(len(changed_location) > 0)

    

class TestImage(TestCase):
    def setUp(self):
        self.nairobi = Location(name='Nairobi')
        self.nairobi.save_location()

        self.travelling = Category(name='Travel')
        self.travelling.save_category()

        self.sample_image = Image(id=1, name='image', description='new image', location=self.nairobi, category=self.travelling)
    
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete() 

    def test_instance(self):
        self.assertTrue(isinstance(self.sample_image, Image))

    def test_save_image(self):
        self.sample_image.save_image()
        imagesaved = Image.objects.all()
        self.assertTrue(len(imagesaved) > 0)

    def test_delete_image(self):
        self.sample_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.sample_image.save_image()
        self.sample_image.update_image(self.sample_image.id, 'photos/image1.jpg')
        new_image = Image.objects.filter(image='photos/image1.jpg')
        self.assertTrue(len(new_image) > 0) 

    def test_get_image_by_id(self):
        myimage = self.sample_image.get_image_by_id(self.sample_image.id)
        image = Image.objects.filter(id=self.sample_image.id)
        self.assertTrue(myimage, image)

    def test_filter_by_location(self):
        self.sample_image.save_image()
        loc_images = self.sample_image.filter_by_location(location='Nairobi')
        self.assertTrue(len(loc_images) == 1)

    def test_search_image(self):
        category = 'Travel'
        cat_images = self.sample_image.search_image(category)
        self.assertTrue(len(cat_images) > 1) 