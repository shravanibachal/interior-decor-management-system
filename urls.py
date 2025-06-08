"""
URL configuration for DelReyDecors project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from DelReyDecors import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cabin/',views.cabin_gallery,name="cabin"),
    path('conference/',views.conference_gallery,name="conference"),
    path('breakroom/',views.breakroom_gallery,name="breakroom"),
    path('reception/',views.reception_gallery,name="reception"),
    path('kitchen/',views.kitchen_gallery,name="kitchen"),
    path('livingroom/',views.livingroom_gallery,name="livingroom"),
    path('bathroom/',views.bathroom_gallery,name="bathroom"),
    path('bedroom/',views.bedroom_gallery,name="bedroom"),
    path('residential/',views.residential_gallery,name="residential"),
    path('commercial/',views.commercial_gallery,name="comercial"),
    path('login/',views.LoginPage,name="login"),
    path('signup/',views.SignupPage,name="signup"),
    path('login/signup/', views.LoginPage, name='login'),
    path('about/',views.About,name="about"),
    path('services/',views.services,name="services"),
    path('display/', views.display, name='display'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('reachoutform/', views.reachout_form_view, name='design_form'),
    
    
    
   


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
