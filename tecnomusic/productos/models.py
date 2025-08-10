from django.db import models # Importamos el módulo models de Django

class Producto(models.Model): # Modelo para representar un producto
   # Definimos los campos del modelo
   nombre = models.CharField(max_length=100, unique=True)  # nombre del producto
   descripcion = models.TextField(blank=True) # Descripción del producto
   precio = models.DecimalField(max_digits=10, decimal_places=2) # Precio del producto
   cantidad_stock = models.PositiveBigIntegerField(default=0) # Cantidad en stock
   fecha_creacion = models.DateTimeField(auto_now_add=True) # Fecha de creación del producto
   fecha_ultima_modificacion = models.DateTimeField(auto_now=True) # Fecha de última modificación del producto

   def __str__(self):
       return self.nombre

   class Meta:
       db_table = 'productos'  # aquí definimos el nombre exacto de la tabla
