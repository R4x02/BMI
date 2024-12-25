from django import forms
from django.contrib.auth.models import User
from .models import Profile

class FormularzRejestracji(forms.ModelForm):
    password2 = forms.CharField(label="Powtórz hasło", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email']
        widgets = {
            'password': forms.PasswordInput,
        }

class BMIForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['wzrost', 'waga']
        widgets = {
            'wzrost': forms.NumberInput(attrs={'step': '0.01'}),
            'waga': forms.NumberInput(attrs={'step': '0.1'}),
        }