from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class FormularzRejestracji(UserCreationForm):
    username = forms.CharField(
        label="Nazwa użytkownika",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Adres e-mail",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class BMIForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['wzrost', 'waga']
        widgets = {
            'wzrost': forms.NumberInput(attrs={'step': '0.01'}),
            'waga': forms.NumberInput(attrs={'step': '0.1'}),
        }