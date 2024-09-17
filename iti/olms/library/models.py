from django.contrib.auth.models import User
from django.db import models


class S(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    student_id = models.IntegerField(unique=True, null=True)
    student_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.student_name




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


class BorrowRecord(models.Model):
    student = models.ForeignKey(S, on_delete=models.CASCADE,related_name='BorrowRecord')
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='BorrowRecord')
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.student} borrowed {self.book}'

