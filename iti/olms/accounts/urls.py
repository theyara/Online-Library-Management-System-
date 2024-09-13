from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.general_login_register, name='general_login_register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
]
