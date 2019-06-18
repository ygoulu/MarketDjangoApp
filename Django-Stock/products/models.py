from django.db import models

# Create your models here.
class Tipo(models.Model):
    nombre_tipo = models.CharField(max_length=100, primary_key=True)

class Articulo(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre_item = models.CharField(max_length=100)
    tipo_item = models.ForeignKey('Tipo',on_delete=models.PROTECT)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad = models.IntegerField()

