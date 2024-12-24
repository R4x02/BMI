from django import forms
from django.contrib.auth.models import User

class FormularzRejestracji(forms.ModelForm):
    password2 = forms.CharField(label="Powtórz hasło", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Hasła nie pasują.")
        return password2
