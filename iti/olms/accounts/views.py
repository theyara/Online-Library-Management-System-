from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def general_login(request):
    return render(request, 'registration/login.html')


def general_register(request):
    return render(request, 'register.html')


def register_admin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            return redirect('login_admin')
    else:
        form = UserCreationForm()
    return render(request, 'register_admin.html', {'form': form})


def register_student(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_student')
    else:
        form = UserCreationForm()
    return render(request, 'register_student.html', {'form': form})


def login_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password or unauthorized access.')
    return render(request, 'accounts/admin_login.html')


def login_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and not user.is_staff:
            login(request, user)
            return redirect('student_dashboard')
        else:
            messages.error(request, 'Invalid username or password or unauthorized access.')
    return render(request, 'accounts/student_login.html')


@login_required
def admin_dashboard(request):
    if request.user.is_staff:
        return render(request, 'a_dashboard.html')
    return redirect('general_login')


@login_required
def student_dashboard(request):
    if not request.user.is_staff:
        return render(request, 'student_dashboard.html')
    return redirect('general_login')


def custom_logout(request):
    logout(request)
    return redirect('general_login')
