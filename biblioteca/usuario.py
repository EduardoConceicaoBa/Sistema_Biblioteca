# Criação da classe usuario
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    # Condição para pegar os livros
    def pegar_livro(self, livro):
        if livro.disponivel:
            livro.emprestar(self.nome)
            self.livros_emprestados.append(livro)
            print(f"{self.nome} pegou o livro '{livro.titulo}'")
        else:
            print("Livro indisponível")
    # Cpndição para devolver os livros
    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            print(f"{self.nome} devolveu '{livro.titulo}'")
        else:
            print("Esse usuário não possui esse livro")