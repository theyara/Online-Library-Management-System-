from django.contrib import admin
from .models import Book,Category
from spanel.models import Student

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Student)


# Register your models here.
