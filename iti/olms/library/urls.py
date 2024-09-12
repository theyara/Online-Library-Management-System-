from django.urls import path
from  .views import (index , register_view , logout_view , login_view ,
                     history_view , profile_view, books)

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('history/', history_view, name='history'),
    path('books/',books , name='books'),
]