from django.contrib import admin
from django.urls import path, include  # Certifique-se de incluir 'include'
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para acessar o Django Admin
    path('api/', include('noticias.urls')),  # Inclui as rotas da aplicação 'noticias'
]

# Servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)