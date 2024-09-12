from django.urls import path
from .views import *

urlpatterns = [
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('register/admin/', register_admin, name='register_admin'),
    path('register/success/', register_success, name='register_success'),
    path('admin/login/',admin_login, name='admin_login'),
]