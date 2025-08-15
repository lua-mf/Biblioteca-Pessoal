import os
def adicionar(livros):
    livro = {}
    nome = input('nome: ')
    livro['nome'] = nome
    autor = input('autor: ')
    livro['autor'] = autor
    categoria = input('categoria: ')
    livro['categoria'] = categoria
    valor = float(input('valor: '))
    livro['valor'] = valor

    livros.append(livro)
    return 'Livro Adicionado com Sucesso!'


def visualizar_todos(livros):
    print('--------- Todos os Livros ---------\n')
    if os.path.getsize('data/biblioteca.txt') != 0:
        with open("data/biblioteca.txt", "r") as f:
            for linha in f:
                print(linha[0])
            
    if len(livros) != 0:
        for i in range(len(livros)):
            print(livros[i].get('nome'))
        

def filtrar_por_categoria(livros):
    categoria = input('categoria: ')
    if os.path.getsize('data/biblioteca.txt') != 0:
        with open("data/biblioteca.txt", "r") as f:
            for linha in f:
                livro = linha.split(',')
                if livro[2].strip() == categoria:
                    print(livro[0].strip())

    if len(livros) != 0:
        for i in range(len(livros)):
            if livros[i].get('categoria') == categoria:
                print(livros[i].get('nome'))


def extrato_por_categoria(livros):
    categorias = {}
    for i in range(len(livros)):
        if livros[i].get('categoria') not in categorias:
            categorias[livros[i].get('categoria')] = livros[i].get('valor')
        else:
            soma = categorias[livros[i].get('categoria')]
            categorias[livros[i].get('categoria')] = (
                soma + livros[i].get('valor')
            )
    for categoria in categorias:
        print(f'{categoria}: R$ {categorias[categoria]:.2f}')


def controle_de_gastos(livros):
    soma = 0
    if os.path.getsize('data/biblioteca.txt') != 0:
        with open("data/biblioteca.txt", "r") as f:
            for linha in f:
                livro = linha.split(',')
                soma += float(livro[3].strip())
    if len(livros) != 0:
        for i in range(len(livros)):
            soma += livros[i].get('valor')
        print(f'R$ {soma:.2f}')
