from django.urls import path
from .views import *

urlpatterns =[
    path('home/', view_home),
    path('lista_de_pratos/', pagina_pratos),
    path('pagina_cadastro/', pagina_cadastro),
    path('cadastrar_prato/', cadastrar_prato, name='cadastrar'),
]