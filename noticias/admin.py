from django.contrib import admin
from .models import Noticia

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date')
    search_fields = ('title', 'content')

admin.site.register(Noticia, NoticiaAdmin)
