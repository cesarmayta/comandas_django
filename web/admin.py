from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Marca)
admin.site.register(Seccion)
admin.site.register(Envase)
admin.site.register(Producto)
