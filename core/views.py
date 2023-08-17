from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def view_home(request):
    return render(request, 'home.html')

def pagina_pratos(request):
    # 1 - Pegar a lista de pratos do banco de dados
    pratos = Prato.objects.all()

    # 2 - Renderizar a página passando os pratos para o template
    return render(request, 'pratos.html', {'pratos': pratos})

def pagina_cadastro(request):
    return render(request, 'cadastro_pratos.html')

def cadastrar_prato(request):
    # 1 - Recebendo valores do request e salvando em variáveis
    novo_nome = request.POST['nome_produto']
    nova_descricao = request.POST['descricao_produto']
    novo_preco = request.POST['preco_produto']

    # 2 - Cadastrar o prato no banco de dados
    # INSERT do SQL
    Prato.objects.create(nome=novo_nome, descricao=nova_descricao, preco=novo_preco)

    return redirect(pagina_cadastro)