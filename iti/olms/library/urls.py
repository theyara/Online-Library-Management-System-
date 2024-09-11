from django.urls import path
from  .views import (index , register_view , logout_view , login_view ,
                     history_view , profile_view, books,register_admin,register_student)

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('register/student/', register_student, name='register_student'),
    path('register/admin/', register_admin, name='register_admin'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('history/', history_view, name='history'),
    path('books/',books , name='books'),
]