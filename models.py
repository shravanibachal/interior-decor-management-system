# models.py
from django.db import models

class Feedback(models.Model):
    email = models.EmailField()
    rating = models.PositiveSmallIntegerField()  # 1 to 5 for star rating
    message = models.TextField()

    def __str__(self):
        return f"Feedback from {self.email} - Rating: {self.rating}"
