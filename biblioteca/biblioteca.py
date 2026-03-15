import json

# Criação da classe biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    # salvar dados em JSON
    def salvar_dados(self):
        dados = {

            "livros": [
                {
                    "titulo": livro.titulo,
                    "autor": livro.autor,
                    "disponivel": livro.disponivel,
                    "emprestado_para": livro.emprestado_para
                }

                for livro in self.livros
            ],

            "usuarios": [
                {
                    "nome": usuario.nome
                }

                for usuario in self.usuarios
            ]
        }

        with open("data/dados.json", "w") as arquivo:
            json.dump(dados, arquivo, indent=4)

        print("Dados salvos com sucesso")

    # adicionar livro (Tratamento para livro duplicado)
    def adicionar_livro(self, livro):
        for l in self.livros:
            if l.titulo.lower() == livro.titulo.lower():
                print("Esse livro já está cadastrado")
                return
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca")


    # buscar livro
    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None


    # cadastrar usuário (Tratamento para cadastro duplicado)
    def cadastrar_usuario(self, usuario):
        for u in self.usuarios:
            if u.nome.lower() == usuario.nome.lower():
                print("Usuário já cadastrado")
                return
        self.usuarios.append(usuario)
        print(f"Usuário '{usuario.nome}' cadastrado")


    # buscar usuário
    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.nome.lower() == nome.lower():
                return usuario
        return None


    # listar livros
    def listar_livros(self):
        print("\nLivros da biblioteca:\n")
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else f"Emprestado para {livro.emprestado_para}"
            print(f"{livro.titulo} - {livro.autor} ({status})")