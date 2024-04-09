from django.urls import path
from .views import home, login_view as login, register_view as register, logout_view as logout

app_name = 'users'
urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout')
]