from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets 
from .models import Objetivo, PesoIdeal, PlanAlimentacion, Ejercicio, Rutina 
from .serializers import ( ObjetivoSerializer, 
    PesoIdealSerializer,
    PlanAlimentacionSerializer,
    EjercicioSerializer,
    RutinaSerializer,
)

class ObjetivoViewSet(viewsets.ModelViewSet):
    queryset = Objetivo.objects.all()
    serializer_class = ObjetivoSerializer

class PesoIdealViewSet(viewsets.ModelViewSet):
    queryset = PesoIdeal.objects.all()
    serializer_class = PesoIdealSerializer

class PlanAlimentacionViewSet(viewsets.ModelViewSet):
    queryset = PlanAlimentacion.objects.all()
    serializer_class = PlanAlimentacionSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

class RutinaViewSet(viewsets.ModelViewSet):
    queryset = Rutina.objects.all()
    serializer_class = RutinaSerializer