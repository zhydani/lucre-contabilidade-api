# Generated by Django 5.1.1 on 2024-09-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Imagem'),
        ),
    ]
