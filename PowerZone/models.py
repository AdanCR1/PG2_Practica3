from django.db import models

class Objetivo(models.Model): 
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class PesoIdealHombre(models.Model): 
    estatura_min = models.DecimalField(max_digits=4, decimal_places=2, help_text="Estatura mínima en metros", null=True, blank=True)
    estatura_max = models.DecimalField(max_digits=4, decimal_places=2, help_text="Estatura máxima en metros", null=True, blank=True)
    edad = models.PositiveIntegerField(help_text="Edad en años", null=True, blank=True)
    peso_min = models.DecimalField(max_digits=5, decimal_places=2, help_text="Peso mínimo en kg", null=True, blank=True)
    peso_max = models.DecimalField(max_digits=5, decimal_places=2, help_text="Peso máximo en kg", null=True, blank=True)
    fotos = models.ImageField(upload_to='fotos/', blank=True, null=True)
    horas_sueno = models.DecimalField(max_digits=3, decimal_places=1)
    dieta = models.TextField()

    def __str__(self):
        return f"{self.peso_min} - {self.peso_max}kg - {self.estatura_min} - {self.estatura_max}cm"
    
class PesoIdealMujer(models.Model): 
    estatura_min = models.DecimalField(max_digits=4, decimal_places=2, help_text="Estatura mínima en metros", null=True, blank=True)
    estatura_max = models.DecimalField(max_digits=4, decimal_places=2, help_text="Estatura máxima en metros", null=True, blank=True)
    edad = models.PositiveIntegerField(help_text="Edad en años", null=True, blank=True)
    peso_min = models.DecimalField(max_digits=5, decimal_places=2, help_text="Peso mínimo en kg", null=True, blank=True)
    peso_max = models.DecimalField(max_digits=5, decimal_places=2, help_text="Peso máximo en kg", null=True, blank=True)
    fotos = models.ImageField(upload_to='fotos/', blank=True, null=True)
    horas_sueno = models.DecimalField(max_digits=3, decimal_places=1)
    dieta = models.TextField()

    def __str__(self):
        return f"{self.peso_min} - {self.peso_max}kg - {self.estatura_min} - {self.estatura_max}cm"

class PlanAlimentacion(models.Model): 
    objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE, related_name='planes', null=True, blank=True)
    calorias_dia = models.PositiveIntegerField(null=True, blank=True, help_text="Calorías totales en gramos")
    proteinas_dia = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Proteínas totales en gramos")

    def __str__(self):
        return f"Plan de Alimentación para {self.objetivo.nombre if self.objetivo else 'Sin Objetivo'}"

class Alimento(models.Model):
    nombre = models.CharField(max_length=100)
    calorias_por_100g = models.FloatField(null=True, blank=True)
    proteinas_por_100g = models.FloatField(null=True, blank=True)
    grasas_por_100g = models.FloatField(null=True, blank=True)
    carbohidratos_por_100g = models.FloatField(null=True, blank=True)
    nota = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class detallePlan(models.Model):
    plan_alimentacion = models.ForeignKey(PlanAlimentacion, on_delete=models.CASCADE, related_name='detalles', null=True, blank=True)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE, related_name='detalles', null=True, blank=True)
    cantidad_proteina_gramos = models.FloatField(null=True, blank=True)
    momento_dia = models.CharField(max_length=20, choices=[
        ('desayuno', 'Desayuno'),
        ('almuerzo', 'Almuerzo'),
        ('cena', 'Cena'),
    ], null=True, blank=True)

    def __str__(self):
        return f"Detalle de Plan: {self.plan_alimentacion} - {self.alimento}"

class Ejercicio(models.Model): 
    grupo_muscular = models.CharField(max_length=100)
    usa_mancuernas = models.BooleanField(null=True, blank=True)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos", default=30)
    gif = models.ImageField(upload_to='ejercicios/', blank=True, null=True)
    descripcion = models.TextField(null=True, blank=True)
    peso_ideal_hombre = models.ForeignKey(PesoIdealHombre, on_delete=models.CASCADE, related_name='ejercicios_recomendados', null=True, blank=True)
    peso_ideal_mujer = models.ForeignKey(PesoIdealMujer, on_delete=models.CASCADE, related_name='ejercicios_recomendados', null=True, blank=True)

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