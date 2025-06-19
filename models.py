from django.db import models

class ProjectSubmission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    payment_mode = models.CharField(max_length=50)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    selected_spaces = models.TextField()  # Should contain space names
    selected_services = models.TextField()  # Should contain service names

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class UploadedImage(models.Model):
    project_submission = models.ForeignKey(ProjectSubmission, related_name='uploaded_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return f"Image for {self.project_submission.first_name} {self.project_submission.last_name} - {self.image.name}"
