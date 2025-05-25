from django.db import models

# Create your models here.

class Breakroom_Img1(models.Model):
    breakroom_img1= models.ImageField(upload_to="photos/", blank=True,null=True)

class Breakroom_Img2(models.Model):
    breakroom_img2= models.ImageField(upload_to="photos/", blank=True,null=True)


class Breakroom_Img3(models.Model):
    breakroom_img3= models.ImageField(upload_to="photos/", blank=True,null=True)

class Breakroom_Img4(models.Model):
    breakroom_img4= models.ImageField(upload_to="photos/", blank=True,null=True)

