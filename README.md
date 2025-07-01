# PowerZone API

## Descripción

PowerZone es una API pública desarrollada en Django y Django REST Framework para la gestión de usuarios, rutinas de ejercicio, ejercicios, categorías, objetivos y planes de alimentación. Permite a los usuarios consultar, crear, modificar y eliminar información relacionada con el fitness y la nutrición.

---

## Instalación y configuración

### 1. Crear y activar el entorno virtual

En Windows:

```sh
python -m venv venv
venv\Scripts\activate
```

En Linux/Mac:

```sh
python3 -m venv venv
source venv/bin/activate
```

### 2. Crear proyecto Django

```sh
django-admin startproject homeFit
```
### 3. Crear aplicación Django

```sh
django-admin startapp PowerZone
```

### 4. Crear archivo `requirements.txt`
```bash
asgiref==3.8.1
Django==5.2.1 # versión estable de Django
django-extensions==4.1 #importante para generar el diagrama de modelos
sqlparse==0.5.3
tzdata==2025.2
djangorestframework==3.16.0 # para crear la API
pillow==10.0.0 # para manejar imágenes
```

### 5. Instalar dependencias

```sh
pip install -r requirements.txt
```

### 6. Configurar `settings.py`
En el archivo `settings.py`, agregar la aplicación `PowerZone`, `rest_framework` y `django_extensions` a la lista de `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'PowerZone',
    'rest_framework',
    'django_extensions',
]
```

### 7. Migrar la base de datos

```sh
python manage.py makemigrations
python manage.py migrate
```

## Diagrama de modelos
Instalar Graphviz desde su [página oficial](https://graphviz.gitlab.io/download/) para generar el diagrama de modelos:

```sh
sudo apt-get install graphviz
```

El diagrama de modelos se genera con el comando:

```sh
python manage.py graph_models PowerZone -o diagrama.png
```

![](diagrama.png)

---

### Ejecutar el servidor

```sh
python manage.py runserver
```

---

## Endpoints de la API

Todos los endpoints están bajo el prefijo `/api/`.  
La API sigue el estándar REST y soporta los métodos GET, POST, PUT/PATCH y DELETE donde corresponda.  
**Todos los datos se envían y reciben en formato JSON.**

---

1. Objetivos
GET /api/objetivos/

```json
[
    {
        "id": 1,
        "nombre": "Pérdida de peso",
        "descripcion": "Objetivo para perder peso de forma saludable."
    }
]
```

POST /api/objetivos/
```json
{
    "nombre": "Aumento de masa muscular",
    "descripcion": "Objetivo para aumentar la masa muscular."
}
```

---

2. Peso Ideal para Hombres
GET /api/pesoidealHombre/

```json
[
    {
        "id": 1,
        "estatura minima": 1.50,
        "estatura maxima": 1.60,
        "edad": 25,
        "peso minimo": 50.0,
        "peso maximo": 56.0,
        "horas_sueno": 7.5,
        "dieta": "Dieta balanceada con énfasis en proteínas."
    }
]
```

POST /api/pesoideal/
```json
{
    "estatura minima": 1.60,
    "estatura maxima": 1.70,
    "edad": 25,
    "peso minimo": 58.0,
    "peso maximo": 65.0,
    "foto": "https://example.com/foto_hombre.jpg",
    "horas_sueno": 8.0,
    "dieta": "Dieta alta en carbohidratos."
}
```
---

3. Peso Ideal para Mujeres
GET /api/pesoidealMujer/
```json
[
    {
        "id": 1,
        "estatura minima": 1.50,
        "estatura maxima": 1.60,
        "edad": 25,
        "peso minimo": 48.0,
        "peso maximo": 55.0,
        "horas_sueno": 7.5,
        "dieta": "Dieta balanceada con énfasis en hierro."
    }
]
```

POST /api/pesoidealMujer/
```json
{
    "estatura minima": 1.60,
    "estatura maxima": 1.70,
    "edad": 25,
    "peso minimo": 55.6,
    "peso maximo": 63.0,
    "foto": "https://example.com/foto_mujer.jpg",
    "horas_sueno": 8.0,
    "dieta": "Dieta alta en calcio."
}
```

---

4. Plan de Alimentación
GET /api/planes/

```json
[
    {
        "id": 1,
        "calorias_dia": 2000,
        "proteinas_dia": 150.0,
    }
]
```

POST /api/planes/
```json
{
    "calorias_dia": 2500,
    "proteinas_dia": 180.0,
}
```

---

5. Ejercicios
GET /api/ejercicios/

```json
[
    {
        "id": 1,
        "grupo_muscular": "Pecho",
        "usa manquernas": true,
        "duracion (minutos)": 30,
        "descripcion": "Press de banca con mancuernas.",
        "peso_ideal": 70.0,
    }
]
```
    
POST /api/ejercicios/
```json
{
    "grupo_muscular": "Espalda",
    "usa mancuernas": true,
    "duracion (minutos)": 30,
    "gif": "https://example.com/remo_mancuernas.gif",
    "descripcion": "Remo con mancuernas.",
    "peso_ideal": 70.0
}
```

---

6. Rutinas
GET /api/rutinas/
```json
[
    {
        "id": 1,
        "veces entrenar dia": 3,
        "veces entrenar semana": 5,
        "comidas dia": 5,
        "tipo de entrenamiento": "Fuerza",
        "objetivo": 1,
    }
]
```

POST /api/rutinas/
```json
{
    "veces entrenar dia": 4,
    "veces entrenar semana": 6,
    "comidas dia": 6,
    "tipo de entrenamiento": "Resistencia",
    "objetivo": 2
}
```

---

7. Alimentos
GET /api/alimentos/
```json
[
    {
        "id": 1,
        "nombre": "Pollo",
        "calorias por 100g": 165,
        "proteinas por 100g": 31.0,
        "grasas por 100g": 6.6,
        "carbohidratos por 100g": 41.25,
        "nota": "Ideal para dietas altas en proteínas."
    }
]
```

POST /api/alimentos/
```json
{
    "nombre": "Salmón",
    "calorias por 100g": 206,
    "proteinas por 100g": 22.1,
    "grasas por 100g": 13.4,
    "carbohidratos por 100g": 51.5,
    "nota": "Rico en ácidos grasos omega-3."
}
```

---

8. Detalle de Plan de Alimentación
GET /api/detalleplan/

```json
[
    {
        "id": 1,
        "cantidad proteinas (gramos)": 30.0,
        "momento del dia": "Desayuno",
        "plan alimentacion": 1,
        "alimento": "Huevos revueltos"
    }
]
```

POST /api/detalleplan/
```json
{
    "cantidad proteinas (gramos)": 25.0,
    "momento del dia": "Almuerzo",
    "plan alimentacion": 1,
    "alimento": "Pechuga de pollo"
}
``` 
---

## Notas

- Todos los endpoints aceptan y devuelven datos en formato JSON.
- Para autenticación y permisos, se puede extender la configuración según las necesidades del proyecto.
- El diagrama de modelos (`diagrama.png`) se generó usando Django Extensions y muestra las relaciones entre las entidades principales del sistema.

---