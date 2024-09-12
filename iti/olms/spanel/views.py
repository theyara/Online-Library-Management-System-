from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def register_student(request):
    if request.method == 'POST':
        student_name = request.POST['student_name']
        student_email = request.POST['student_email']
        student_password = request.POST['student_password']
        confirm_password = request.POST['confirm_password']
        if student_password == confirm_password:
            user = User.objects.create(username=student_name, email=student_email,
                                       password=make_password(student_password))
            user.save()
            return redirect('register_success')
        else:
            return render(request, 'register_student.html', {'error': 'Passwords do not match'})

    return render(request, 'register_student.html')


def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None and Student.objects.filter(user=user).exists():
            login(request, user)
            return redirect('student_dashboard')
        else:
            messages.error(request, 'Invalid credentials or not a student')
            return redirect('student_login')

    return render(request, 'accounts/student_login.html')


@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

# Create your views here.
