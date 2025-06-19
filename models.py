from django.db import models

class ReachoutForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    spaces = models.TextField()  # Storing multiple spaces as comma-separated values
    services = models.TextField()  # Storing multiple services as comma-separated values
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_mode = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Picture(models.Model):
    reachout_form = models.ForeignKey(ReachoutForm, related_name='pictures', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pictures/')  # Path for the image upload

    def __str__(self):
        return f"Image for {self.reachout_form.first_name} {self.reachout_form.last_name}"
