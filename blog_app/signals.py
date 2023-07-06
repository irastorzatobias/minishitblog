from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Entrada, Comentario


@receiver(post_save, sender=Entrada)
def update_entradas_count(sender, instance, created, **kwargs):
    if created:
        instance.autor.entradas_count += 1
        instance.autor.save()


@receiver(post_save, sender=Comentario)
def update_comentarios_count(sender, instance, created, **kwargs):
    if created:
        instance.entrada.comentarios_count += 1
        instance.entrada.save()
