import utils
import file_manager
import os
os.system("cls")


def main():
    # lista de dicionarios, cada dicionario é um livro
    livros = []

    while True:
        # CRUD
        print('\n--------- Menu ---------\n 1 - Adicionar\n 2 - Visualizar\n 3 - Atualizar\n 4 - Excluir\n 5 - Sair')
        resposta_1 = int(input())
        if resposta_1 == 1:
            resultado = utils.adicionar(livros)
            print(resultado)
        elif resposta_1 == 2:
            print(
                'a) Todos os livros\nb) Filtrar por categoria\nc) Extrato por categoria\nd) Controle de Gastos')
            resposta_2 = input()
            if resposta_2 == 'a':
                utils.visualizar_todos(livros)
            elif resposta_2 == 'b':
                utils.filtrar_por_categoria(livros)
            elif resposta_2 == 'c':
                utils.extrato_por_categoria(livros)
            elif resposta_2 == 'd':
                utils.controle_de_gastos(livros)
        elif resposta_1 == 5:
            file_manager.salvar_livros(livros)
            break


if __name__ == "__main__":
    main()
