def adicionar(livros):
    nome = input('nome: ')
    livros['nome'].append(nome)
    autor = input('autor: ')
    livros['autor'].append(autor)
    categoria = input('categoria: ')
    livros['categoria'].append(categoria)
    valor = input('valor: ')
    livros['valor'].append(valor)
    return 'Livro Adicionado com Sucesso!'


def vizualizar_todos(livros):
    print('--------- Todos os Livros ---------\n')
    for nome in livros.get('nome'):
        print(nome)


def filtrar_por_categoria(livros):
    categoria = input('categoria: ')
    indice = -1
    for valor in livros['categoria']:
        indice += 1
        if valor == categoria:
            print(livros['nome'][indice])
