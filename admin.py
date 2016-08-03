from django.contrib import admin

# Register your models here.
from .models import Galleta, Proveedor, Sabor


admin.site.register([Galleta, Proveedor, Sabor])