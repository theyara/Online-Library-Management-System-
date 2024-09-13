from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 related_name='Book', blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


@property
def image_url(self):
    return f'/media/{self.image}'


class S(models.Model):
    user = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.user.username

class BorrowRecord(models.Model):
    student = models.ForeignKey(S, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.student} borrowed {self.book}'
# Create your models here.
