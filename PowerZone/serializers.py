from rest_framework import serializers
from .models import Objetivo, PesoIdealHombre, PesoIdealMujer, PlanAlimentacion, Ejercicio, Rutina, Alimento, detallePlan

class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objetivo
        fields = '__all__'

class PesoIdealHombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PesoIdealHombre
        fields = '__all__'

class PesoIdealMujerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PesoIdealMujer
        fields = '__all__'

class PlanAlimentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanAlimentacion
        fields = '__all__'

class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = '__all__'

class DetallePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = detallePlan
        fields = '__all__'

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'

class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = '__all__'