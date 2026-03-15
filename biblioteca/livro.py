# Criação da classe Livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        self.emprestado_para = None


    # emprestar livro
    def emprestar(self, usuario):
        if self.disponivel:
            self.disponivel = False
            self.emprestado_para = usuario
            print(f"O livro '{self.titulo}' foi emprestado para {usuario}")
        else:
            print("O livro já foi emprestado")


    # devolver livro
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            self.emprestado_para = None
            print(f"O livro '{self.titulo}' foi devolvido")