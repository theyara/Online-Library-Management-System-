from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



def general_login_register(request):
    # Handle login and registration for both student and admin
    if request.method == 'POST':
        if 'login' in request.POST:
            # Login process
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_type = request.POST.get('user_type')  # Check if the user is admin or student
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user_type == 'admin' and user.is_staff:
                    return redirect('admin_dashboard')
                elif user_type == 'student' and not user.is_staff:
                    return redirect('student_dashboard')
                else:
                    # Invalid user type (admin/student mismatch)
                    return render(request, 'accounts/general_login_register.html', {'error': 'Invalid user type'})
            else:
                return render(request, 'accounts/general_login_register.html', {'error': 'Invalid credentials'})
        elif 'register' in request.POST:
            # Registration process
            form = UserCreationForm(request.POST)
            user_type = request.POST.get('user_type')
            if form.is_valid():
                user = form.save(commit=False)
                if user_type == 'admin':
                    user.is_staff = True  # Make the user an admin
                user.save()
                return redirect('general_login_register')
            else:
                return render(request, 'accounts/general_login_register.html', {'form': form, 'error': 'Registration failed'})
    else:
        form = UserCreationForm()

    return render(request, 'accounts/general_login_register.html', {'form': form})



@login_required
def admin_dashboard(request):
    if request.user.is_staff:
        return render(request, 'a_dashboard.html')
    else:
        return redirect('accounts/general_login_register')  # Redirect if not admin

@login_required
def student_dashboard(request):
    if not request.user.is_staff:
        return render(request, 'student_dashboard.html')
    else:
        return redirect('accounts/general_login_register')  # Redirect if not student
