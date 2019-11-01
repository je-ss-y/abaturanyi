from django.db import models

# Create your models here.


class Location(models.Model):
    umujyi = models.CharField(max_length =30)
    umurenge = models.CharField(max_length =30)
    

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()


    def save_editor(self):
        self.delete()

