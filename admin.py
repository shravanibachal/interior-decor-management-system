
# admin.py
from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'rating', 'message')

admin.site.register(Feedback, FeedbackAdmin)
