from django.urls import path
from . import views
urlpatterns = [
    path('cars/', views.get_cars, name='list-cars'),
    path('brands/', views.get_brands, name="list-brands")
] 