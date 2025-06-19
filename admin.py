from django.contrib import admin
from django.utils.html import format_html
from .models import ProjectSubmission, UploadedImage

class UploadedImageInline(admin.TabularInline):
    model = UploadedImage
    extra = 1  # Allows adding extra image fields

class ProjectSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 
        'last_name', 
        'email', 
        'phone', 
        'payment_mode', 
        'total_cost', 
        'display_selected_spaces', 
        'display_selected_services', 
        'display_uploaded_images'
    )
    inlines = [UploadedImageInline]

    def display_selected_spaces(self, obj):
        return obj.selected_spaces.replace(',', ', ') if obj.selected_spaces else "None"
    display_selected_spaces.short_description = 'Selected Spaces'

    def display_selected_services(self, obj):
        return obj.selected_services.replace(',', ', ') if obj.selected_services else "None"
    display_selected_services.short_description = 'Selected Services'

    def display_uploaded_images(self, obj):
        images_html = ''
        for img in obj.uploaded_images.all():
            images_html += format_html('<img src="{}" style="width: 150px; height: auto; margin-right: 10px;" />', img.image.url)
        return format_html(images_html) if images_html else "No Images"
    display_uploaded_images.short_description = 'Uploaded Images'

admin.site.register(ProjectSubmission, ProjectSubmissionAdmin)
