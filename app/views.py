from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def centros(request):
    return render(request, 'app/centros.html')

def login(request):
    return render(request, 'app/login.html')

def hora(request):
    return render(request, 'app/hora.html')
    

