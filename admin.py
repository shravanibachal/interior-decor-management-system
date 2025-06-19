from django.contrib import admin
from .models import ReachoutForm, Picture
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

class ReachoutFormAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'spaces', 'services', 'total_cost', 'payment_mode']
    inlines = [PictureInline]

    def spaces(self, obj):
        return obj.spaces

    def services(self, obj):
        return obj.services

# Register ReachoutForm model
admin.site.register(ReachoutForm, ReachoutFormAdmin)

# Register Picture model separately
class PictureAdmin(admin.ModelAdmin):
    list_display = ['reachout_form', 'image_display']

    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="150" />', obj.image.url)
        return "No image available"

    image_display.short_description = "Uploaded Image"

admin.site.register(Picture, PictureAdmin)
