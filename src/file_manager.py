def salvar_livros(livros):
    with open("data/biblioteca.txt", "a") as f:
        f.writelines(livros)
