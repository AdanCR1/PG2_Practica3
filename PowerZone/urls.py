from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from .views import ( ObjetivoViewSet, PesoIdealHombreViewSet, PesoIdealMujerViewSet, PlanAlimentacionViewSet, EjercicioViewSet, RutinaViewSet, AlimentoViewSet, DetallePlanViewSet )

router = DefaultRouter()
router.register(r'objetivos', ObjetivoViewSet)
router.register(r'pesoidealHombre', PesoIdealHombreViewSet)
router.register(r'pesoidealMujer', PesoIdealMujerViewSet)
router.register(r'planes', PlanAlimentacionViewSet)
router.register(r'ejercicios', EjercicioViewSet)
router.register(r'rutinas', RutinaViewSet)
router.register(r'alimentos', AlimentoViewSet)
router.register(r'detalleplan', DetallePlanViewSet)

urlpatterns = [ path('', include(router.urls)), ]