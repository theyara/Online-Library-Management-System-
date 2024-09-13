from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import AdminRegistrationForm
from .models import Admin
from .forms import StudentSearchForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from library.models import BorrowRecord
from django.contrib.admin.views.decorators import staff_member_required
from .models import Student

@staff_member_required
def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})


def view_borrowed_books(request):
    borrowed_books = BorrowRecord.objects.select_related('book', 'student').all()
    return render(request, 'books/view_borrowed_books.html', {'borrowed_books': borrowed_books})


def view_all_users(request):
    users = User.objects.all()  # Fetch all user accounts
    return render(request, 'view_all_users.html', {'users': users})


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
