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


---

## Notas

- Todos los endpoints aceptan y devuelven datos en formato JSON.
- Para autenticación y permisos, se puede extender la configuración según las necesidades del proyecto.
- El diagrama de modelos (`diagrama.png`) se generó usando Django Extensions y muestra las relaciones entre las entidades principales del sistema.

---