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
    for i in range(len(livros)):
        print(livros[i].get('nome'))


def filtrar_por_categoria(livros):
    categoria = input('categoria: ')
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
    print(categorias)


def controle_de_gastos(livros):
    soma = 0
    for i in range(len(livros)):
        soma += livros[i].get('valor')
    print(f'R$ {soma:.2f}')
