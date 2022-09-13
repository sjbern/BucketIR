from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta: #nested namespace to keep configurations in one place
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta: #allows user to update profile information
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm): #allows user to update image
    class Meta:
        model = Profile
        fields = ['image']