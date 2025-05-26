from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    edad = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    objetivo = models.ForeignKey('Objetivo', on_delete=models.SET_NULL, null=True, blank=True)
    plan_alimentacion = models.ForeignKey('PlanAlimentacion', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Ejercicio(models.Model):
    LEVEL_CHOICES = [
        ('principiante', 'Principiante'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]

    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="ejercicios")
    grupo_muscular = models.CharField(max_length=50)
    nivel = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    duracion = models.IntegerField(help_text="Duración en segundos")
    tipo = models.CharField(max_length=30)
    instrucciones = models.TextField()
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Rutina(models.Model):
    nombre = models.CharField(max_length=100)
    ejercicios = models.ManyToManyField(Ejercicio)
    duracion_total = models.IntegerField(help_text="Duración total en minutos", null=True, blank=True)
    objetivo = models.ForeignKey('Objetivo', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Objetivo(models.Model):
    nombre = models.CharField(max_length=100)  # Ejemplo: "Perder peso", "Ganar peso", etc.
    nivel = models.CharField(max_length=50, choices=[
        ("saludable", "Saludable"),
        ("adelgazamiento", "Adelgazamiento"),
        ("fuerza", "Fuerza"),
        ("resistencia", "Resistencia"),
        ("hipertrofia", "Hipertrofia"),
        ("aumento_masa", "Aumento de masa muscular"),
        ("estético", "Estético"),
        ("culturismo", "Culturismo"),
    ])
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.nivel}"

class PlanAlimentacion(models.Model):
    nombre = models.CharField(max_length=100)
    objetivo = models.ForeignKey(Objetivo, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()
    calorias_dia = models.IntegerField()
    duracion_dias = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.objetivo.nombre}"