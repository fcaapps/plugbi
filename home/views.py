from django.shortcuts import render
from contas.models import User

def home(request):
    return render(request, 'home.html')