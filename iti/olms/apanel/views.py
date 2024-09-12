from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .forms import AdminRegistrationForm
from .models import Admin
from django.contrib.auth import authenticate, login
from django.contrib import messages


def register_admin(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            admin_name = form.cleaned_data.get('admin_name')
            admin_email = form.cleaned_data.get('admin_email')
            admin_password = form.cleaned_data.get('admin_password')
            user = User.objects.create(username=admin_name, email=admin_email, password=make_password(admin_password))
            user.save()
            Admin.objects.create(admin_name=user, admin_email=admin_email, admin_password=admin_password)

            return redirect('register_success')
    else:
        form = AdminRegistrationForm()

    return render(request, 'register_admin.html', {'form': form})


def register_success(request):
    return render(request, 'register_success.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None and Admin.objects.filter(user=user).exists():
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid credentials or not an admin')
            return redirect('admin_login')

    return render(request, 'accounts/admin_login.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
# Create your views here.
