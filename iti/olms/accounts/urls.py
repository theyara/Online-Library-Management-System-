from django.urls import path , include
from .views import AccountDetailView

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('dashboard/<int:pk>', AccountDetailView.as_view, name='admin_dashboard'),
]
