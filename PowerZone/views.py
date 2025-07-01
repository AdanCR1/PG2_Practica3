from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets 
from .models import Objetivo, PesoIdealHombre, PesoIdealMujer, PlanAlimentacion, Ejercicio, Rutina, Alimento, detallePlan 
from .serializers import ( ObjetivoSerializer, 
    PesoIdealHombreSerializer,
    PesoIdealMujerSerializer,
    PlanAlimentacionSerializer,
    EjercicioSerializer,
    RutinaSerializer,
    AlimentoSerializer,
    DetallePlanSerializer
)

class ObjetivoViewSet(viewsets.ModelViewSet):
    queryset = Objetivo.objects.all()
    serializer_class = ObjetivoSerializer

class PesoIdealHombreViewSet(viewsets.ModelViewSet):
    queryset = PesoIdealHombre.objects.all()
    serializer_class = PesoIdealHombreSerializer

class PesoIdealMujerViewSet(viewsets.ModelViewSet):
    queryset = PesoIdealMujer.objects.all()
    serializer_class = PesoIdealMujerSerializer

class PlanAlimentacionViewSet(viewsets.ModelViewSet):
    queryset = PlanAlimentacion.objects.all()
    serializer_class = PlanAlimentacionSerializer

class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer

class DetallePlanViewSet(viewsets.ModelViewSet):
    queryset = detallePlan.objects.all()
    serializer_class = DetallePlanSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

class RutinaViewSet(viewsets.ModelViewSet):
    queryset = Rutina.objects.all()
    serializer_class = RutinaSerializer