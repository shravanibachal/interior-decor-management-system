from django.db import models

# Create your models here.
class Reception_Img1(models.Model):
    reception_img1= models.ImageField(upload_to="photos/", blank=True,null=True)

class Reception_Img2(models.Model):
     reception_img2= models.ImageField(upload_to="photos/", blank=True,null=True)


class Reception_Img3(models.Model):
     reception_img3= models.ImageField(upload_to="photos/", blank=True,null=True)

class Reception_Img4(models.Model):
     reception_img4= models.ImageField(upload_to="photos/", blank=True,null=True)
