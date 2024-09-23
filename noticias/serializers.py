from rest_framework import serializers
from .models import Noticia

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ['id', 'title', 'content', 'image_url', 'post_date']
