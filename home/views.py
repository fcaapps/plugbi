from django.shortcuts import render
from contas.models import User

def home(request):
    user = User.objects.get(email='')
    user.delete()
    return render(request, 'home.html')