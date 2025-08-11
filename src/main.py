import utils
import os
os.system("cls")


def main():
    livro = {
        'nome': [],
        'autor': [],
        'categoria': [],
        'valor': []
    }
    # CRUD
    print('--------- Menu ---------\n 1 - Adicionar\n 2 - Visualizar\n 3 - Atualizar\n 4 - Excluir')
    resposta = int(input())
    if resposta == 1:
        resultado = utils.adicionar(livro)
        print(resultado)


if __name__ == "__main__":
    main()
