from django.db import models
# Django ya tiene usuario incorporado
from django.contrib.auth.models import AbstractUser


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Entrada(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey('blog_app.CustomUser', on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    comentarios_count = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey('blog_app.CustomUser', on_delete=models.CASCADE)
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto


class CustomUser(AbstractUser):
    entradas_count = models.IntegerField(default=0)
