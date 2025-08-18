def salvar_livros(livros):
    with open("data/biblioteca.txt", "a", encoding="utf-8") as arquivo:
        for livro in livros:
            arquivo.write(f"{livro['nome']}, {livro['autor']}, {livro['categoria']}, {livro['valor']}\n")
        
