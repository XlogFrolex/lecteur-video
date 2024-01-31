# pylint: disable=import-error
# monapp/urls.py

from django.urls import path
from .views import lecteur

urlpatterns = [
    path('', lecteur, name="lecteursimple"),
]