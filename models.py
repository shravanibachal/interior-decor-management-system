from django.db import models

# Create your models here.

class Aboutimage1(models.Model):
     aboutimage1= models.ImageField(upload_to="photos/", blank=True,null=True)
     
class Aboutimage2(models.Model):
     aboutimage2= models.ImageField(upload_to="photos/", blank=True,null=True)

