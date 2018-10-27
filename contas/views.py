from django.shortcuts import render, redirect
from django.contrib.auth import logout

def contas(request):
    return render(request, 'contas.html')

def logout_sistema(request):
    logout(request)
    return redirect('home')
