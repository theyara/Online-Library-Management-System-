from django import forms
from django.contrib.auth.models import User


class StudentSearchForm(forms.Form):
    student_id = forms.CharField(label='Student ID', max_length=100)


class AdminRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
