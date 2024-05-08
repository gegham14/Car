from django.urls import path
from . import views

urlpatterns = [
    path('manufactures', views.manufactures),
    path('cars', views.cars),
]