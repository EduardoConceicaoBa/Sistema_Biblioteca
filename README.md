# 📚 Sistema de Biblioteca (CLI)

Este é um projeto em **Python** que implementa um sistema simples de gerenciamento de biblioteca utilizando **Programação Orientada a Objetos (POO)**.

O sistema funciona através do **terminal (CLI)** e permite cadastrar livros, cadastrar usuários, emprestar livros e registrar devoluções.

O objetivo do projeto é **praticar conceitos fundamentais de Python e POO**, além de organização de código em múltiplos arquivos.

---

# 🚀 Funcionalidades

O sistema apresenta um menu interativo com as seguintes opções:

### 📖 Cadastrar Livro
Permite adicionar um novo livro informando:

- título
- autor

O sistema impede o cadastro de livros duplicados.

---

### 👤 Cadastrar Usuário

Permite registrar novos usuários na biblioteca.

O sistema também verifica se o usuário já está cadastrado.

---

### 📚 Listar Livros

Exibe todos os livros cadastrados junto com seu status:

- ✅ Disponível
- 📕 Emprestado para algum usuário

---

### 🔄 Emprestar Livro

Permite que um usuário pegue um livro disponível.

Caso o livro já esteja emprestado, o sistema informa que ele está indisponível.

---

### ↩️ Devolver Livro

Permite que um usuário devolva um livro que foi emprestado.

O sistema verifica se o usuário realmente possui aquele livro.

---

### 💾 Salvar e Sair

Antes de encerrar o programa, os dados são salvos automaticamente em um arquivo JSON.

---

# 🛠️ Tecnologias e Conceitos Utilizados

Para construir este projeto foram utilizados conceitos fundamentais de programação:

## 🐍 Python

Linguagem principal utilizada para implementar toda a lógica do sistema.

---

## 🧠 Programação Orientada a Objetos (POO)

O projeto utiliza três classes principais:

### Classe `Livro`

Responsável por representar um livro da biblioteca.

**Atributos:**

- `titulo`
- `autor`
- `disponivel`
- `emprestado_para`

**Métodos:**

- `emprestar()`
- `devolver()`

---

### Classe `Usuario`

Representa um usuário do sistema.

**Atributos:**

- `nome`
- `livros_emprestados`

**Métodos:**

- `pegar_livro()`
- `devolver_livro()`

---

### Classe `Biblioteca`

Responsável por gerenciar todo o sistema.

Funções principais:

- adicionar livros
- cadastrar usuários
- buscar livros
- buscar usuários
- listar livros

---

## 💾 Persistência de Dados

Os dados da biblioteca são armazenados em um arquivo JSON:

data/dados.json


Isso permite que as informações não sejam perdidas quando o programa é encerrado.

---



---

# 📖 Como Usar

## Pré-requisitos

Ter instalado:


Python 3.x


---

## Execução

1. Clone o repositório:


2. Entre na pasta do projeto:


3. Execute o programa:


  python main.py


---



---

# 📋 Regras de Negócio

O sistema possui verificações para evitar erros:

- ✔ Evita cadastro de livros duplicados
- ✔ Evita cadastro de usuários duplicados
- ✔ Não permite emprestar livros indisponíveis
- ✔ Usuários só podem devolver livros que pegaram

---

# 💡 Sugestões de Evolução

Possíveis melhorias futuras para o projeto:

- 🔎 Busca de livros por título ou autor
- 📜 Histórico de empréstimos
- 📊 Estatísticas da biblioteca
- 🖥️ Interface gráfica usando **Tkinter**
- 🌐 Versão web usando **Flask ou Django**

---

# 👨‍💻 Autor

Desenvolvido por **Eduardo**

Projeto criado para estudo de **Python e Programação Orientada a Objetos**.
