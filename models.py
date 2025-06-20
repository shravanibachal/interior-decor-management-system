from django.db import models

# Create your models here.
class Residential_Img1(models.Model):
    residential_img1= models.ImageField(upload_to="photos/", blank=True,null=True)

class Residential_Img2(models.Model):
    residential_img2= models.ImageField(upload_to="photos/", blank=True,null=True)

class Residential_Img3(models.Model):
     residential_img3= models.ImageField(upload_to="photos/", blank=True,null=True)

class Residential_Img4(models.Model):
     residential_img4= models.ImageField(upload_to="photos/", blank=True,null=True)

class Residential_Img5(models.Model):
     residential_img5= models.ImageField(upload_to="photos/", blank=True,null=True)

