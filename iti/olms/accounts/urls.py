from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.general_login, name='general_login'),
    path('register/', views.general_register, name='general_register'),
    path('register/admin/', views.register_admin, name='register_admin'),
    path('register/student/', views.register_student, name='register_student'),
    path('login/admin/', views.login_admin, name='login_admin'),
    path('login/student/', views.login_student, name='login_student'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('logout/', views.custom_logout, name='logout'),
]
