from django.db import models

# Create your models here.

class Cabin_Img1(models.Model):
    cabin_img1= models.ImageField(upload_to="photos/", blank=True,null=True)

class Cabin_Img2(models.Model):
    cabin_img2= models.ImageField(upload_to="photos/", blank=True,null=True)


class Cabin_Img3(models.Model):
    cabin_img3= models.ImageField(upload_to="photos/", blank=True,null=True)

class Cabin_Img4(models.Model):
    cabin_img4= models.ImageField(upload_to="photos/", blank=True,null=True)

