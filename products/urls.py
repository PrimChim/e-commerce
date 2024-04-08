from django.urls import path
from .views import add_product

app_name = 'products'
urlpatterns = [
    path('add/', add_product, name='add_product'),
]