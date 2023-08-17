from django.urls import path
from .views import view_home, pagina_pratos

urlpatterns =[
    path('home/', view_home),
    path('lista_de_pratos/', pagina_pratos)
]