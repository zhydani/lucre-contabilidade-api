from django.db import models
from ckeditor.fields import RichTextField

class Noticia(models.Model):
    title = models.CharField("Título", max_length=255)
    content = RichTextField("Conteúdo")
    image = models.ImageField("Imagem", upload_to='noticias/', blank=True, null=True)
    post_date = models.DateField("Data de publicação")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"


