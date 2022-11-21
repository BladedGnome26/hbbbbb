from django.db import models
from django.db.models.fields import TextField, DateField, CharField, EmailField
from django.db.models.fields.related import ForeignKey
# Create your models here.
class puntos(models.Model):
    nombrePunto = models.CharField(max_length=100, verbose_name="Nombre punto de reciclaje", blank=False, null=False)
    direccionPunto = models.CharField(max_length=250, verbose_name="Dirección punto de reciclaje", blank=False, null=False)
    descripcionPunto = models.TextField(verbose_name="Descripción punto de reciclaje", blank=False, null=False)
    lngLat = models.CharField(max_length=700, verbose_name="Latitud y Longitud ubicación", blank=False, null=False)

    def __str__(self):
        return self.nombrePunto

class comentarios(models.Model):
    idPunto = models.ForeignKey(puntos, on_delete=models.CASCADE, blank=False, null=False)
    valoracion = models.IntegerField(verbose_name="Puntaje de valoración", blank=False, null=False)
    comentarios = TextField(verbose_name="Comentario")

    def __str__(self):
        return "Comentario de punto: "+str(self.idPunto.nombrePunto)


