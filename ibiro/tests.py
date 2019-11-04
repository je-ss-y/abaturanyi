from django.test import TestCase
from .models import Location,Profile


class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Location(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Location))



    # Testing Save Method
    def test_save_method(self):
        self.james.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

     # Testing Save Method
    def test_delete_method(self):
        self.james.delete_editor()
        locations = Location.objects.all()
        self.assertTrue(len(locations) ==0)

class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Profile(user = 'James', bio ='Muriuki', profilepicture ='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Location))



    # Testing Save Method
    def test_save_method(self):
        self.james.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

     # Testing Save Method
    def test_delete_method(self):
        self.james.delete_editor()
        locations = Location.objects.all()
        self.assertTrue(len(locations) ==0)