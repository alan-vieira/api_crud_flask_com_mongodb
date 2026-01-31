# 📚 API CRUD: Gestão de Livros com Flask & MongoDB

## 📖 Sobre o Projeto

Esta aplicação é um exemplo prático de como construir uma **API RESTful** para gerenciamento de um acervo literário. O objetivo principal é demonstrar a integração entre Python e bancos de dados orientados a documentos (NoSQL), permitindo operações dinâmicas em uma coleção de livros.

## 🛠️ Funcionalidades Implementadas

- **Criar (POST)**: Adiciona novos títulos à coleção do MongoDB.
- **Ler (GET)**: Consulta a lista completa de livros ou busca um título específico via ID.
- **Atualizar (PUT)**: Edita informações de registros já existentes.
- **Excluir (DELETE)**: Remove livros da base de dados de forma definitiva.

## 📂 Estrutura de Arquivos

- `app.py`: O script principal que contém as rotas e a lógica da API.

- `mongopass.py`: Gerenciamento de credenciais para conexão segura com o MongoDB Atlas.

- `livros.json`: Exemplo da estrutura de dados utilizada nos documentos.

- `curl_command.txt`: Documentação de comandos para testes manuais dos endpoints.

- `requirements.txt`: Lista de dependências (Flask 2.2.2, PyMongo 4.3.3).

## 🚀 Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/alan-vieira/api_crud_flask_com_mongodb.git

2. Instale as bibliotecas necessárias:

   ```bash
   pip install -r requirements.txt

3. Configure sua URI de conexão no arquivo `mongopass.py`.

4. Inicie o servidor:

   ```bash
   python app.py

## 🧪 Testando a API

Você pode utilizar o Postman, Insomnia ou os comandos contidos no arquivo curl_command.txt para validar cada uma das rotas criadas.
 
## 📺 Demonstração

Acompanhe a explicação técnica detalhada no YouTube:

🔗 [Assistir vídeo explicativo](https://www.youtube.com/watch?v=neQ1RF-3B4U)

## 👤 Autor

**Alan Vieira** - *Engenheiro de Telecomunicações & Especialista em Dados*

- [LinkedIn](https://www.linkedin.com/in/alansilvavieira)

- [GitHub Portfólio](https://github.com/alan-vieira)
