📚 Sistema de Biblioteca (CLI)

Sistema de gerenciamento de biblioteca desenvolvido em Python utilizando Programação Orientada a Objetos (POO).
O projeto roda no terminal e permite cadastrar livros, cadastrar usuários, realizar empréstimos e registrar devoluções.

Além de funcionar como um pequeno sistema de gerenciamento, o objetivo principal do projeto é praticar conceitos fundamentais de POO e organização de código em Python.

🚀 Funcionalidades

O sistema possui um menu interativo no terminal com as seguintes opções:

Cadastrar Livro
Permite adicionar um novo livro informando título e autor.

Cadastrar Usuário
Permite registrar um novo usuário no sistema.

Listar Livros
Exibe todos os livros cadastrados na biblioteca junto com seu status:

Disponível

Emprestado para algum usuário

Emprestar Livro
Permite que um usuário pegue um livro disponível.

Devolver Livro
Permite que um usuário devolva um livro que foi emprestado.

Salvar e Sair
Os dados são salvos automaticamente em um arquivo JSON antes do sistema ser encerrado.

🛠️ Tecnologias e Conceitos Utilizados

Para construir este projeto foram aplicados diversos conceitos importantes:

Python

Linguagem principal utilizada para implementar toda a lógica do sistema.

Programação Orientada a Objetos (POO)

O projeto utiliza os principais pilares da POO:

Classes

Livro

Usuario

Biblioteca

Objetos

Cada livro e cada usuário cadastrado se torna um objeto dentro do sistema.

Atributos

Exemplos:

titulo

autor

disponivel

emprestado_para

Métodos


📋 Menu do Sistema

Ao executar o programa, o seguinte menu será exibido:

=== SISTEMA DA BIBLIOTECA ===

1 - cadastrar livro
2 - cadastrar usuario
3 - listar livros
4 - emprestar livro
5 - devolver livro
6 - sair

O usuário pode escolher uma opção digitando o número correspondente.

📋 Regras de Negócio

O sistema possui algumas verificações para evitar erros comuns:

Evitar livros duplicados

Não é possível cadastrar dois livros com o mesmo título.

Evitar usuários duplicados

O sistema verifica se o usuário já está cadastrado.

Controle de disponibilidade

Um livro só pode ser emprestado se estiver disponível.

Controle de devolução

Um usuário só pode devolver um livro que ele realmente tenha emprestado.


💡 Sugestões de Evolução

Algumas melhorias que podem ser implementadas no futuro:

Carregar dados automaticamente

Implementar leitura do dados.json ao iniciar o sistema.

Busca de livros

Permitir buscar livros por título ou autor.

Histórico de empréstimos

Registrar quais livros cada usuário já pegou.

Interface gráfica

Transformar o sistema em uma aplicação visual utilizando bibliotecas como:

Tkinter

PyQt

CustomTkinter

👨‍💻 Autor

Desenvolvido por Eduardo
Projeto criado para estudo de Python e Programação Orientada a Objetos.
