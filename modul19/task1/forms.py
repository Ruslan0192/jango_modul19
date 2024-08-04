from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2= forms.CharField(widget=forms.PasswordInput())
    balance = forms.DecimalField(max_digits=20, decimal_places=2)
