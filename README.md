📚 Sistema de Biblioteca (Python + POO)

Um sistema simples de gerenciamento de biblioteca no terminal, desenvolvido em Python utilizando Programação Orientada a Objetos (POO).

O objetivo deste projeto é praticar conceitos fundamentais da programação orientada a objetos, organizando o código em classes e simulando o funcionamento básico de uma biblioteca.

🚀 Funcionalidades

O sistema permite:

📖 Cadastrar livros

👤 Cadastrar usuários

📋 Listar livros cadastrados

📦 Emprestar livros

🔁 Devolver livros

💾 Salvar os dados da biblioteca em JSON

🧠 Conceitos de POO aplicados

Durante o desenvolvimento foram utilizados conceitos importantes de Programação Orientada a Objetos:

Classes

Livro

Usuario

Biblioteca

Atributos

Exemplo da classe Livro:

titulo
autor
disponivel
emprestado_para

Exemplo da classe Usuario:

nome
livros_emprestados

Exemplo da classe Biblioteca:

livros
usuarios
Métodos

Alguns métodos implementados no projeto:

emprestar()
devolver()
pegar_livro()
devolver_livro()
adicionar_livro()
buscar_livro()
cadastrar_usuario()
listar_livros()
salvar_dados()

Esses métodos permitem que os objetos interajam entre si, simulando o funcionamento de uma biblioteca real.

📂 Estrutura do Projeto
biblioteca-poo
│
├── biblioteca
│   ├── __init__.py
│   ├── biblioteca.py
│   ├── livro.py
│   └── usuario.py
│
├── data
│   └── dados.json
│
├── main.py
├── README.md
└── .gitignore


📌 Tecnologias utilizadas

Python 3

Programação Orientada a Objetos (POO)

JSON para armazenamento de dados

🎯 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de:

praticar Programação Orientada a Objetos

aprender a organizar projetos Python

trabalhar com múltiplas classes

simular um sistema simples de gerenciamento

🔮 Possíveis melhorias futuras

Algumas melhorias que podem ser implementadas no futuro:

carregar os dados automaticamente ao iniciar o programa

adicionar interface gráfica

usar banco de dados

criar autenticação de usuários

adicionar testes automatizados

👨‍💻 Autor
Eduardo Conceição de Barros

Projeto desenvolvido para estudo de Python e Programação Orientada a Objetos.