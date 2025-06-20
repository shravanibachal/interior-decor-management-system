from django.db import models

class ResidentialFormSubmission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_mode = models.CharField(max_length=100)
    selected_spaces = models.TextField()
    selected_services = models.TextField()

    def get_selected_spaces(self):
        return self.selected_spaces.split(', ')

    def get_selected_services(self):
        return self.selected_services.split(', ')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Picture(models.Model):
    submission = models.ForeignKey(ResidentialFormSubmission, related_name='pictures', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')


    def __str__(self):
        return f"Image for {self.submission}"
