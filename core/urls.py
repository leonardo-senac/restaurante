from django.urls import path
from .views import *

urlpatterns =[
    path('home/', view_home),
    path('lista_de_pratos/', pagina_pratos),
    path('pagina_cadastro/', pagina_cadastro),
    path('cadastrar_prato/', cadastrar_prato, name='cadastrar'),
    path('pagina_cadastro_comanda/', pagina_cadastro_comanda),
    path('cadastro_comanda/', cadastro_comanda, name='cadastro_comanda')
]