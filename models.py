from django.db import models

# Create your models here.
class Conference_Img1(models.Model):
    conference_img1= models.ImageField(upload_to="photos/", blank=True,null=True)

class Conference_Img2(models.Model):
    conference_img2= models.ImageField(upload_to="photos/", blank=True,null=True)


class Conference_Img3(models.Model):
    conference_img3= models.ImageField(upload_to="photos/", blank=True,null=True)

class Conference_Img4(models.Model):
    conference_img4= models.ImageField(upload_to="photos/", blank=True,null=True)

