from django.contrib import admin
from .models import Comanda, Pedido, Prato

# Register your models here.

admin.site.register(Comanda)
admin.site.register(Pedido)
admin.site.register(Prato)