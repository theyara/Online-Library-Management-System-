from django.urls import path , include
from .views import AccountDetailView , admin_login

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('admin/login', admin_login, name='admin_login'),
    path('dashboard/<int:pk>', AccountDetailView.as_view, name='a_dashboard'),
]
