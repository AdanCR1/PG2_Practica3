from django.urls import path, include
from rest_framework.routers import DefaultRouter # type: ignore
from .views import (
    UsuarioViewSet, EjercicioViewSet, CategoriaViewSet,
    RutinaViewSet, ObjetivoViewSet, PlanAlimentacionViewSet
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'ejercicios', EjercicioViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'rutinas', RutinaViewSet)
router.register(r'objetivos', ObjetivoViewSet)
router.register(r'planes', PlanAlimentacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]