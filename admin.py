from django.contrib import admin
from .models import ResidentialFormSubmission, Picture
from django.utils.html import format_html

class PictureInline(admin.TabularInline):
    model = Picture
    extra = 1
    readonly_fields = ['display_image']

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="150" />', obj.image.url)
        return "No image available"

    display_image.short_description = "Uploaded Image"

class ResidentialFormSubmissionAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 
        'last_name', 
        'email', 
        'phone', 
        'total_cost', 
        'payment_mode', 
        'display_selected_spaces', 
        'display_selected_services'
    ]
    inlines = [PictureInline]

    def display_selected_spaces(self, obj):
        return ', '.join(obj.get_selected_spaces())
    display_selected_spaces.short_description = 'Selected Spaces'

    def display_selected_services(self, obj):
        return ', '.join(obj.get_selected_services())
    display_selected_services.short_description = 'Selected Services'

# Register the models to the admin panel
admin.site.register(ResidentialFormSubmission, ResidentialFormSubmissionAdmin)

# Register the Picture model with custom image display
class PictureAdmin(admin.ModelAdmin):
    list_display = ['residential_form', 'image_display']

    def residential_form(self, obj):
        return obj.submission  # Display the linked form submission
    
    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="150" />', obj.image.url)
        return "No image available"
    
    image_display.short_description = "Uploaded Image"

admin.site.register(Picture, PictureAdmin)
