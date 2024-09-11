from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):
    admin_name = models.OneToOneField(User, on_delete=models.CASCADE)
    admin_email = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)

    def __str__(self):
        return self.admin_name

# Create your models here.
