from django.db import models

# Create your models here.


class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    provedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="productos")

    def __str__(self):
        return self.nombre