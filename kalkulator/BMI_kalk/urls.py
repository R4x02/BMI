from django.urls import path
from .views import rejestracja, WidokLogowania
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('rejestracja/', rejestracja, name='rejestracja'),
    path('logowanie/', WidokLogowania.as_view(), name='logowanie'),
    path('wylogowanie/', LogoutView.as_view(), name='wylogowanie'),
]
