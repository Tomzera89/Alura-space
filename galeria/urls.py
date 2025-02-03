from django.urls import path
from galeria.views import index

urlpatterns = [
    path('', index, name='index'),
    # Add more URL patterns as needed
]