from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import FormularzRejestracji, BMIForm
from .models import Profile
from django.views import View


# Widok logowania
class WidokLogowania(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'logowanie.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('strona_glowna')
        return render(request, 'logowanie.html', {'form': form})


# Widok rejestracji
def rejestracja(request):
    if request.method == 'POST':
        formularz_uzytkownika = FormularzRejestracji(request.POST)
        if formularz_uzytkownika.is_valid():
            uzytkownik = formularz_uzytkownika.save()
            login(request, uzytkownik)
            return redirect('strona_glowna')
    else:
        formularz_uzytkownika = FormularzRejestracji()

    return render(request, 'rejestracja.html', {'formularz_uzytkownika': formularz_uzytkownika})

#Widok strony głównej
@login_required
def strona_glowna(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    bmi = None
    kategoria = None
    if profile.wzrost and profile.waga:
        bmi, kategoria = profile.oblicz_bmi()

    if request.method == 'POST':
        form = BMIForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            bmi, kategoria = profile.oblicz_bmi()
            return render(request, 'baza.html', {'form': form, 'bmi': bmi, 'kategoria': kategoria})
    else:
        form = BMIForm(instance=profile)

    return render(request, 'baza.html', {'form': form, 'bmi': bmi, 'kategoria': kategoria})

#Wylogowywanie
def wylogowanie(request):
    logout(request)
    return redirect('logowanie')