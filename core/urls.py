from django.urls import path
from .views import *

urlpatterns =[
    path('home/', view_home),
    path('lista_de_pratos/', pagina_pratos),
    path('pagina_cadastro/', pagina_cadastro),
    path('cadastrar_prato/', cadastrar_prato, name='cadastrar'),
    path('pagina_cadastro_comanda/', pagina_cadastro_comanda),
    path('cadastro_comanda/', cadastro_comanda, name='cadastro_comanda'),
    path('pagina_cadastro_pedidos/', pagina_cadastro_pedidos),
    path('cadastrar_pedido/', cadastrar_pedido, name='cadastrar_pedido'),
    path('lista_de_pedidos/', lista_de_pedidos),
    path('fechar_pedido/<int:id_pedido>', fechar_pedido, name='fechar_pedido'),
    path('pagina_inserir_produto_no_pedido/<int:id_pedido>', pagina_inserir_produto_no_pedido, name='pagina_inserir_produto_no_pedido'),
    path('salvar_produto_no_pedido/<int:id_pedido>', salvar_produto_no_pedido, name='salvar_produto_no_pedido')
]