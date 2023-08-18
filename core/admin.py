from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Comanda)
admin.site.register(Pedido)
admin.site.register(Prato)
admin.site.register(pratos_pedidos)