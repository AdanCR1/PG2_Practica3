from rest_framework import serializers
from .models import Objetivo, PesoIdeal, PlanAlimentacion, Ejercicio, Rutina

class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objetivo
        fields = '__all__'

class PesoIdealSerializer(serializers.ModelSerializer):
    class Meta:
        model = PesoIdeal
        fields = '__all__'

class PlanAlimentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanAlimentacion
        fields = '__all__'

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'

class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = '__all__'