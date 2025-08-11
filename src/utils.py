def adicionar(livro):
    nome = input('nome: ')
    livro['nome'].append(nome)
    autor = input('autor: ')
    livro['autor'].append(autor)
    categoria = input('categoria: ')
    livro['categoria'].append(categoria)
    valor = input('valor: ')
    livro['valor'].append(valor)
    return 'Livro Adicionado com Sucesso!'
