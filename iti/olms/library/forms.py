from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_title(self):
        name = self.cleaned_data['title']
        book_name = Book.objects.filter(title=name).exists()
        if book_name:
            raise forms.ValidationError("Book with this title already exists")
        return name


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
