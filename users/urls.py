from django.urls import path
from .views import home, login_view as login

app_name = 'users'
urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
]