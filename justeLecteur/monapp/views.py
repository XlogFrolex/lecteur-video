# pylint: disable=import-error
from django.shortcuts import render

# Create your views here.

def lecteur(request):
    return render(request, 'index.html')
