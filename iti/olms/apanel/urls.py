from django.urls import path
from .views import *

urlpatterns = [
    path('register/success/', register_success, name='register_success'),
    path('search-student/', search_student, name='search_student'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('password-change-done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('users/', view_all_users, name='view_all_users'),
    path('borrowed-books/', view_borrowed_books, name='view_borrowed_books'),
    path('students/', view_students, name='view_students'),
]