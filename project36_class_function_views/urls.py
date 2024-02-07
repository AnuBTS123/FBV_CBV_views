"""
URL configuration for project36_class_function_views project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv_string/',fbv_string,name='fbv_string'),
    path('CBVString/',CBVString.as_view(),name='CBVString'),

    path('fbvhtml/',fbvhtml,name='fbvhtml'),
    path('cbvhtml/',cbvhtml.as_view(),name='cbvhtml'),

    path('insert_school_by_fbv/',insert_school_by_fbv,name='insert_school_by_fbv'),
    path('insert_school_by_Cbv/',insert_school_by_Cbv.as_view(),name='insert_school_by_Cbv'),
    

]