from django import forms
from django.contrib.auth.models import User


class AdminRegistrationForm(forms.ModelForm):
    admin_password = forms.CharField(widget=forms.PasswordInput, label="admin_password")

    class Meta:
        model = User
        fields = ['admin_name', 'admin_email']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
