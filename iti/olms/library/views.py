from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def books(request):
    books = [
        {"name": "How Innovation Works", "auther": " Matt Ridley ",
         "description": "Innovation is an evolutionary process. The starting ingredients are freedom and a basic level of prosperity within society",
         "image": "img1 (2).jpg"},
        {"name": "The phsycology of Money", "auther": " Morgan Housel ",
         "description": "Overall: The Psychology of Money is a refreshing and insightful book that offers a unique perspective on the relationship between money and human behavior.",
         "image": "img2 (2).jpg"},
        {"name": "Hooked", "auther": " Nir Eyal ",
         "description": "This book offers invaluable insights into the psychology behind creating products that captivate and retain users. Highly recommended for anyone involved in product development.",
         "image": "img3 (3).jpg"},
        {"name": "Seeds Planted in Concrete", "auther": " Bianca Sparacino ",
         "description": "This collection is a manifesto of the journey every human being takes throughout their life; an assembly of words that celebrates the resilience of the human heart through stages of hurting, feeling, healing and loving. Bianca Sparacino?s first collection of work is one that will speak to the very depths of those who read it, inspiring a will to love, and live.",
         "image": "img4 (3).jpg"},
    ]
    return render(request, 'books.html', {'books': books})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_role = request.POST['role']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user_role == 'admin':
                return redirect('admin_dashboard')
            elif user_role == 'student':
                return redirect('student_dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


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


def register_admin(request):
    if request.method == 'POST':
        admin_name = request.POST['admin_name']
        admin_email = request.POST['admin_email']
        admin_password = request.POST['admin_password']

        user = User.objects.create(username=admin_name, email=admin_email, password=make_password(admin_password))
        user.save()

        return redirect('register_success')

    return render(request, 'register_admin.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile_view(request):
    return render(request, 'profile.html')


@login_required
def history_view(request):
    # Assuming you have a model for keeping history
    return render(request, 'history.html')

# Create your views here.
