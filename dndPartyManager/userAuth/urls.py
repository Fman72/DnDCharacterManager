from django.urls import path, include
from rest_framework import routers
from .views import currentUser


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('currentUser', currentUser), 
]