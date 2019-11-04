from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Location(models.Model):
    umujyi = models.CharField(max_length =30)
    umurenge = models.CharField(max_length =30)
    

    def __str__(self):
        return self.umurenge

    def save_editor(self):
        self.save()


    def save_editor(self):
        self.delete()


class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField()
    profilepicture= models.ImageField(upload_to='profile/', blank=True)


    def __str__(self):
        return self.profilepicture




class Snap(models.Model):
    image=  models.ImageField(upload_to='images/', blank=True)
    photoname = models.TextField()
    description =models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
    
    
    # profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

    


    def __str__(self):
        return self.snap




