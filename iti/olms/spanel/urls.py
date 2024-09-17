from django.urls import path
from . import views

urlpatterns = [
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/login', views.student_login, name='student_login'),
    path('borrowedbooks/', views.borrowed_books_for_std , name='borrowedbooks_for_std'),
]