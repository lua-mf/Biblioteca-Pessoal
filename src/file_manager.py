import os
def salvar_biblioteca(livros):
    with open("data/biblioteca.txt", "a", encoding="utf-8") as arquivo:
        for livro in livros:
            arquivo.write(f"{livro['nome']}, {livro['autor']}, {livro['categoria']}, {livro['valor']}\n")
        
def carregar_biblioteca():
    livros = []
    try:
        if os.path.getsize("data/biblioteca.txt") == 0:
            print(f"O arquivo biblioteca.txt está vazio.")
            return []
        with open("data/biblioteca.txt", "r", encoding="utf-8") as arquivo:
            for livro in livros:
                livro = livro.split(',')

                dic = {
                    "nome": livro[0].strip(),
                    "autor": livro[1].strip(),
                    "categoria": livro[2].strip(),
                    "valor": livro[3].strip
                }

                livros.append(dic)
        print(f"Biblioteca carregada com sucesso!")
    except FileNotFoundError:
        print(f"Arquivo biblioteca.txt não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return livros
            