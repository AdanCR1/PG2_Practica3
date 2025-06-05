from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from .views import ( ObjetivoViewSet, PesoIdealViewSet, PlanAlimentacionViewSet, EjercicioViewSet, RutinaViewSet )

router = DefaultRouter()
router.register(r'objetivos', ObjetivoViewSet)
router.register(r'pesoideal', PesoIdealViewSet)
router.register(r'planes', PlanAlimentacionViewSet)
router.register(r'ejercicios', EjercicioViewSet)
router.register(r'rutinas', RutinaViewSet)

urlpatterns = [ path('', include(router.urls)), ]