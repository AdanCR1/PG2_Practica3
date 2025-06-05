from django.db import models

class Objetivo(models.Model): 
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

def __str__(self):
    return self.nombre

class PesoIdeal(models.Model): 
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    estatura = models.DecimalField(max_digits=4, decimal_places=2)
    edad = models.PositiveIntegerField()
    fotos = models.ImageField(upload_to='fotos/', blank=True, null=True)
    horas_sueno = models.DecimalField(max_digits=3, decimal_places=1)
    dieta = models.TextField()

def __str__(self):
    return f"{self.peso}kg - {self.estatura}cm"

class PlanAlimentacion(models.Model): 
    objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE, related_name='planes', null=True, blank=True)
    calorias_dia = models.PositiveIntegerField(null=True, blank=True)
    proteinas_dia = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

def __str__(self):
    return f"{self.objetivo.nombre} - {self.calorias_dia} cal"

class Ejercicio(models.Model): 
    grupo_muscular = models.CharField(max_length=100)
    usa_mancuernas = models.BooleanField(null=True, blank=True)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos", default=30)
    gif = models.ImageField(upload_to='ejercicios/', blank=True, null=True)
    descripcion = models.TextField(null=True, blank=True)

def __str__(self):
    return self.grupo_muscular

class Rutina(models.Model): 
    objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE, related_name='rutinas', null=True, blank=True)
    veces_entrenar_dia = models.PositiveIntegerField(null=True, blank=True)
    veces_entrenar_semana = models.PositiveIntegerField(null=True, blank=True)
    comidas_dia = models.PositiveIntegerField(null=True, blank=True)
    tipo_entrenamiento = models.CharField(max_length=100, null=True, blank=True)

def __str__(self):
    return f"Rutina de {self.objetivo.nombre}"