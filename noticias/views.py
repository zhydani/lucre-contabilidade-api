from rest_framework import generics
from .models import Noticia
from .serializers import NoticiaSerializer

class NoticiaListView(generics.ListAPIView):
    queryset = Noticia.objects.all()  
    serializer_class = NoticiaSerializer 