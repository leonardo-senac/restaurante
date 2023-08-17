from django.shortcuts import render
from .models import *

# Create your views here.

def view_home(request):
    return render(request, 'home.html')

def pagina_pratos(request):
    # 1 - Pegar a lista de pratos do banco de dados
    pratos = Prato.objects.all()

    # 2 - Renderizar a página passando os pratos para o template
    return render(request, 'pratos.html', {'pratos': pratos})