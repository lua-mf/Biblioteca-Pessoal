def salvar_livros(livros):
    with open("data/biblioteca.txt", "a") as f:
        for i in range(len(livros)):
            f.write(f'{livros[i].get('nome')}, {livros[i].get('autor')}, {livros[i].get('categoria')}, {livros[i].get('valor')}\n')
