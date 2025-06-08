from django.db import models

# Create your models here.
class Commercial_Img1(models.Model):
    commercial_img1= models.ImageField(upload_to="photos/", blank=True,null=True)

class Commercial_Img2(models.Model):
    commercial_img2= models.ImageField(upload_to="photos/", blank=True,null=True)

class Commercial_Img3(models.Model):
     commercial_img3= models.ImageField(upload_to="photos/", blank=True,null=True)

class Commercial_Img4(models.Model):
     commercial_img4= models.ImageField(upload_to="photos/", blank=True,null=True)

class Commercial_Img5(models.Model):
     commercial_img5= models.ImageField(upload_to="photos/", blank=True,null=True)