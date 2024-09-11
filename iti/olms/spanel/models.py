from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    student_name = models.OneToOneField(User, on_delete=models.CASCADE)
    student_email = models.CharField(max_length=100)
    student_password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name

# Create your models here.
