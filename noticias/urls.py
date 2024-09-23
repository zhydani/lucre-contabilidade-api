from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoticiaViewSet  # Certifique-se de importar a view das notícias

router = DefaultRouter()
router.register(r'noticias', NoticiaViewSet)  # Registrar a rota das notícias

urlpatterns = [
    path('', include(router.urls)),  # Incluir as rotas do router
    # Outras rotas personalizadas
]
