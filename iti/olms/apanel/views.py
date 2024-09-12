from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .forms import AdminRegistrationForm
from .models import Admin
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Student
from .forms import StudentSearchForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy


def search_student(request):
    form = StudentSearchForm(request.GET or None)
    student = None

    if form.is_valid():
        student_id = form.cleaned_data['student_id']
        student = Student.objects.filter(student_id=student_id).first()  # Get the student or None

    return render(request, 'search_student.html', {'form': form, 'student': student})


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'


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

# Create your views here.
