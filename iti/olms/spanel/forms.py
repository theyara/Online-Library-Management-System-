from django import forms
from django.contrib.auth.models import User


class StudentRegistrationForm(forms.ModelForm):
    student_password = forms.CharField(widget=forms.PasswordInput, label="student_password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['student_name', 'student_email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("student_password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
