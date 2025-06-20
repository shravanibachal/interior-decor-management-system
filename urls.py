from django.urls import path
from .import views 

urlpatterns = [
    path('residentialform/', views.residential_form_view, name='submit_residential_form'),
    
]

