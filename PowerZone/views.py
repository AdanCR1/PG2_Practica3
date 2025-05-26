from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets  # type: ignore
from .models import Usuario, Ejercicio, Categoria, Rutina, Objetivo, PlanAlimentacion
from .serializers import (
    UsuarioSerializer, EjercicioSerializer, CategoriaSerializer,
    RutinaSerializer, ObjetivoSerializer, PlanAlimentacionSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class RutinaViewSet(viewsets.ModelViewSet):
    queryset = Rutina.objects.all()
    serializer_class = RutinaSerializer

class ObjetivoViewSet(viewsets.ModelViewSet):
    queryset = Objetivo.objects.all()
    serializer_class = ObjetivoSerializer

class PlanAlimentacionViewSet(viewsets.ModelViewSet):
    queryset = PlanAlimentacion.objects.all()
    serializer_class = PlanAlimentacionSerializer