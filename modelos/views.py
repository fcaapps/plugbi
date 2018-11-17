from django.shortcuts import render

def modelos(request):
    return render(request, 'modelos.html')

def politica(request):
    return render(request, 'politica.html')
