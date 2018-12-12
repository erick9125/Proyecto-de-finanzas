from django.contrib import admin
from .models import Usuarios, Producto, Lista
# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Producto)
admin.site.register(Lista)