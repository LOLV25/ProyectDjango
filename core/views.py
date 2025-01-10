from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .models import Usuario, Estado
from .serializers import UsuarioSerializer, EstadoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

# core/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a la página de inicio!")

