from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book, Category
from .models import S,BorrowRecord


class BorrowBookForm(forms.ModelForm):
    book = forms.ModelChoiceField(
        queryset=Book.objects.all(),
        to_field_name='name',  # Use book name for selection
        label='Select Book'
    )

    class Meta:
        model = BorrowRecord
        fields = ['book']


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = S
        fields = ['student_id']

class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = []


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
