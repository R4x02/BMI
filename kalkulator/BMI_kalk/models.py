from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wiek = models.PositiveIntegerField(null=True, blank=True)
    wzrost = models.FloatField(null=True, blank=True, help_text="Wzrost w metrach (np. 1.8)")
    waga = models.FloatField(null=True, blank=True, help_text="Waga w kilogramach (np. 69)")
    adres = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Profil użytkownika {self.user.username}"

    def oblicz_bmi(self):
        if self.wzrost and self.waga:
            bmi = self.waga / (self.wzrost ** 2)
            bmi_rounded = round(bmi, 2)

            if bmi_rounded < 18.5:
                kategoria = "Niedowaga"
            elif 18.5 <= bmi_rounded < 24.9:
                kategoria = "Waga prawidłowa"
            elif 25 <= bmi_rounded < 29.9:
                kategoria = "Nadwaga"
            else:
                kategoria = "Otyłość"

            return bmi_rounded, kategoria
        return None, None
