# from django.contrib import admin
# from django.utils.html import format_html
# from comform.models import DesignFormSubmission, UploadedImage

# @admin.register(DesignFormSubmission)
# class DesignFormSubmissionAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'phone', 'payment_mode', 'total_cost', 'display_selected_spaces', 'display_selected_services', 'display_uploaded_images')
#     search_fields = ('first_name', 'last_name', 'email')
#     filter_horizontal = ('uploaded_images',)

#     def display_selected_spaces(self, obj):
#         return obj.selected_spaces.replace(',', ', ')  # Display as human-readable list
#     display_selected_spaces.short_description = 'Selected Spaces'

#     def display_selected_services(self, obj):
#         return obj.selected_services.replace(',', ', ')  # Display as human-readable list
#     display_selected_services.short_description = 'Selected Services'

#     def display_uploaded_images(self, obj):
#         # Display images in the admin panel with an <img> tag
#         images_html = ''
#         for img in obj.uploaded_images.all():
#             images_html += format_html('<img src="{}" style="width: 150px; height: auto; margin-right: 10px;" />', img.image.url)
#         return format_html(images_html)
#     display_uploaded_images.short_description = 'Uploaded Images'

#     def get_queryset(self, request):
#         # Optimize queryset by prefetching related uploaded images
#         queryset = super().get_queryset(request)
#         queryset = queryset.prefetch_related('uploaded_images')
#         return queryset

# @admin.register(UploadedImage)
# class UploadedImageAdmin(admin.ModelAdmin):
#     list_display = ('image_preview', 'image_name')

#     def image_preview(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" style="max-width: 200px; max-height: 200px;" />', obj.image.url)
#         return 'No Image'
#     image_preview.short_description = 'Image Preview'

#     def image_name(self, obj):
#         return obj.image.name
#     image_name.short_description = 'Image Name'