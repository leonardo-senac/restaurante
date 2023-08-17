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

def pagina_cadastro_comanda(request):
    return render(request, 'cadastro_comandas.html')

def cadastro_comanda(request):
    nova_comanda = request.POST['numero_comanda']

    Comanda.objects.create(numero=nova_comanda)

    return redirect(pagina_cadastro_comanda)

def pagina_cadastro_pedidos(request):
    # Pegar a lista com todas as comandas
    comandas = Comanda.objects.all()

    # Renderizar a página passando a lista de comandas para o html
    return render(request, 'cadastro_pedidos.html', {'comandas_template':comandas})

def cadastrar_pedido(request):
    # Abrir a carta (requisição) e pegar os valores
    id_comanda = request.POST['comanda_pedido']
    comanda_pedido = Comanda.objects.get(id=id_comanda)

    data_pedido = request.POST['data_pedido']

    # Utilizar os valores resgatados da carta para adicionar um novo pedido ao banco de dados
    Pedido.objects.create(data_pedido=data_pedido, comanda=comanda_pedido, valor_total=0, aberto=True)

    # Dar uma resposta à requisição
    return redirect(pagina_cadastro_pedidos)