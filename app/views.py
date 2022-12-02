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

def nosotros(request):
    return render(request, 'app/nosotros.html')

def especialistas(request): 
    return render(request, 'app/especialistas.html')

def administracion(request):
    return render(request, 'app/administracion.html')

def pago (request):
    return render(request, 'app/pago.html')
    
    

