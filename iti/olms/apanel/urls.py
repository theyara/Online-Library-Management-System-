from django.urls import path
from .views import *

urlpatterns = [
    path('register/admin/', register_admin, name='register_admin'),
    path('register/success/', register_success, name='register_success'),
    path('search-student/', search_student, name='search_student'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('password-change-done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),

]