from biblioteca.livro import Livro
from biblioteca.usuario import Usuario
from biblioteca.biblioteca import Biblioteca

biblioteca = Biblioteca()

while True:

    print("\n=== SISTEMA DA BIBLIOTECA ===")

    print("1 - cadastrar livro")
    print("2 - cadastrar usuario")
    print("3 - listar livros")
    print("4 - emprestar livro")
    print("5 - devolver livro")
    print("6 - sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")

        novo_livro = Livro(titulo, autor)

        biblioteca.adicionar_livro(novo_livro)

    elif opcao == "2":
        nome = input("Nome do usuário: ")

        novo_usuario = Usuario(nome)

        biblioteca.cadastrar_usuario(novo_usuario)

    elif opcao == "3":
        biblioteca.listar_livros()

    elif opcao == "4":
        nome_usuario = input("Nome do usuário: ")
        titulo_livro = input("Título do livro: ")

        usuario = biblioteca.buscar_usuario(nome_usuario)
        livro = biblioteca.buscar_livro(titulo_livro)

        if usuario and livro:
            usuario.pegar_livro(livro)
        else:
            print("Usuário ou livro não encontrado")

    elif opcao == "5":
        nome_usuario = input("Nome do usuário: ")
        titulo_livro = input("Título do livro: ")

        usuario = biblioteca.buscar_usuario(nome_usuario)
        livro = biblioteca.buscar_livro(titulo_livro)

        if usuario and livro:
            usuario.devolver_livro(livro)
        else:
            print("Usuário ou livro não encontrado")

    elif opcao == "6":
        biblioteca.salvar_dados()
        print("Dados salvos. Encerrando sistema...")
        break