from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

# Create your views here.
