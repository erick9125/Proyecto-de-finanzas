from django.db import models
#Modelo usuario de Django
from django.contrib.auth.models import User

#Modelo de Usuarios
class Usuarios(models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length = 50)
    email = models.CharField(max_length = 30, null = True, blank = True)    
    clave = models.CharField(max_length = 30, null = True, blank = True)

#Modelo de Productos
class Lista(models.Model):
    nombrelista = models.CharField(max_length=200, blank='false')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombrelista

class Tienda(models.Model):
    nombretienda = models.CharField(max_length=200, blank='false',unique=True)
    nombresucursal = models.CharField(max_length=200, blank='true')
    esOnline = models.BooleanField()
    direccion = models.CharField(max_length=200, blank='true')
    ciudad = models.CharField(max_length=200, blank='true')
    region = models.CharField(max_length=200, blank='true')
    verificado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombretienda

class Producto(models.Model):
    nombreproducto = models.CharField(max_length=200, blank='true')
    costoP =  models.IntegerField()
    costoR = models.IntegerField()
    tienda = models.ForeignKey(Tienda, null=True ,on_delete=models.SET_NULL)
    lista = models.ForeignKey(Lista, null=True ,on_delete=models.SET_NULL, related_name="relatedlistas")
    notas = models.CharField(max_length=200, blank='true')
    comprado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombreproducto