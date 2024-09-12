from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import AdminLoginForm, StudentLoginForm
from spanel.models import Student
from apanel.models import Admin
from django.views.generic import DetailView
from django.contrib.auth.models import User


class AccountDetailView(DetailView):
    model = User
    template_name = 'apanel/admin_dashboard.html'



def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if Admin.objects.filter(user=user).exists():
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, 'You are not an admin.')
        else:
            messages.error(request, 'Invalid credentials.')
    else:
        form = AdminLoginForm()
    return render(request, 'accounts/admin_login.html', {'form': form})


def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if Student.objects.filter(user=user).exists():
                login(request, user)
                return redirect('student_dashboard')
            else:
                messages.error(request, 'You are not a student.')
        else:
            messages.error(request, 'Invalid credentials.')
    else:
        form = StudentLoginForm()
    return render(request, 'accounts/student_login.html', {'form': form})

# Create your views here.
