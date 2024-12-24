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
