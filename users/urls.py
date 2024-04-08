from django.urls import path
from .views import home

app_name = 'users'
urlpatterns = [
    path('', home, name='home'),
]