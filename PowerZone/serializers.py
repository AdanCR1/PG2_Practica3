from rest_framework import serializers # type: ignore
from django.contrib.auth.models import User
from .models import Usuario, Categoria, Ejercicio, Objetivo, PlanAlimentacion, Rutina

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EjercicioSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()

    class Meta:
        model = Ejercicio
        fields = '__all__'

class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objetivo
        fields = '__all__'

class PlanAlimentacionSerializer(serializers.ModelSerializer):
    objetivo = ObjetivoSerializer()

    class Meta:
        model = PlanAlimentacion
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    objetivo = ObjetivoSerializer()
    plan_alimentacion = PlanAlimentacionSerializer()

    class Meta:
        model = Usuario
        fields = '__all__'

class RutinaSerializer(serializers.ModelSerializer):
    ejercicios = EjercicioSerializer(many=True)
    objetivo = ObjetivoSerializer()

    class Meta:
        model = Rutina
        fields = '__all__'