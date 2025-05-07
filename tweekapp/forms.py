from django import forms
from .models import Tweek
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Form for the Tweek model
class TweekForm(forms.ModelForm):
    class Meta:
        model = Tweek
        fields = ['text', 'photo']

# Corrected User Registration Form
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("full_name","username", "email", "user_photo", "password1", "password2")
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 p-2 rounded',
                'placeholder': 'Enter your Full Name'
            }),
            'username': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 p-2 rounded',
                'placeholder': 'Enter your username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border border-gray-300 p-2 rounded',
                'placeholder': 'Enter your email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'w-full border border-gray-300 p-2 rounded',
                'placeholder': 'Enter your password'
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'w-full border border-gray-300 p-2 rounded'
            }),
        }