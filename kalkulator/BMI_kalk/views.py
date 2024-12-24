from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import FormularzRejestracji
from django.views import View


def rejestracja(request):
    if request.method == 'POST':
        formularz = FormularzRejestracji(request.POST)
        if formularz.is_valid():
            uzytkownik = formularz.save()
            login(request, uzytkownik)
            return redirect('strona_glowna')
    else:
        formularz = FormularzRejestracji()
    return render(request, 'rejestracja.html', {'formularz': formularz})

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

@login_required
def strona_glowna(request):
    return render(request, 'baza.html')
