from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description']
        labels: {'title': 'Title* ', 'description': 'Description* :'}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2']
        labels = {'username': 'Username* :',
                  'email': 'Email* :',
                  'password1': 'Password* :',
                  'password2': 'Confirm Password* :'}

        widgets = {

            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'})

        }


class LoginForm(forms.Form):
    username = forms.CharField(label='Username* :', max_length=40,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password* :', max_length=20,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UpdateUserForm(ModelForm):
    class Meta:
        model = User

        fields = ['username', 'email']
        labels: {'username': 'Username* :', 'email': 'Email* :'}

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
