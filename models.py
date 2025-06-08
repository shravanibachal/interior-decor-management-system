# from django.db import models
# from comform.models import DesignFormSubmission, UploadedImage

# # Create your models here.
# class DesignFormSubmission(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     selected_spaces = models.TextField()  # Store spaces as comma-separated values
#     selected_services = models.TextField()  # Store services as comma-separated values
#     payment_mode = models.CharField(max_length=50)
#     uploaded_images = models.ManyToManyField('UploadedImage', blank=True)  # Use ManyToMany for multiple images
#     total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Store total cost

#     def _str_(self):
#         return f"{self.first_name} {self.last_name} - {self.email}"
    
# class UploadedImage(models.Model):
#     design_submission = models.ForeignKey(DesignFormSubmission, on_delete=models.CASCADE, null=True, blank=True)

#     def _str_(self):
#         return self.image.name