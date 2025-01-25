# Processamento de Documentos com LLM e Web Scraping Recursivo

Este projeto é uma aplicação full-stack construída com Vue 3, Vuetify, Pinia e Flask. Ele permite que os usuários treinem um modelo de linguagem grande (LLM) para processar documentos em formato PDF, TXT e URLs. Além disso, a aplicação inclui funcionalidade de web scraping recursivo para extração de dados de sites.

---

## Funcionalidades

- **Frontend**
  - Construído com Vue 3 e Vuetify para uma interface responsiva.
  - Gerenciamento de estado usando Pinia.
  - Upload de arquivos PDF e TXT para processamento.
  - Entrada de URLs para análise de documentos.
  - Monitoramento em tempo real do progresso do scraping.

- **Backend**
  - Construído com Flask.
  - Integração com LLM para análise de documentos.
  - Web scraping recursivo para extração abrangente de dados.
  - Endpoints de API para comunicação entre frontend e backend.

---

## Pré-requisitos

1. **Frontend**:
   - Node.js (v16 ou superior)
   - npm ou yarn

2. **Backend**:
   - Python 3.8+
   - Ferramentas de ambiente virtual (e.g., `venv` ou `virtualenv`)

---

## Estrutura do Projeto

```plaintext
project-root/
├── backend/
│   ├── app.py              # Ponto de entrada do Flask
│   ├── requirements.txt   # Dependências do Python
│   └── venv/              # Ambiente virtual
├── frontend/
│   ├── src/
│   │   ├── components/ # Componentes Vue
│   │   ├── stores/     # Stores Pinia
│   │   ├── views/      # Views Vue
│   │   └── App.vue     # Arquivo principal Vue
│   └── package.json         # Dependências do frontend
└── README.md            # Documentação do projeto
```

---

## Configuração e Uso

### Backend

1. Navegue até o diretório `backend`:
   ```bash
   cd backend
   ```

2. Crie e ative um ambiente virtual:
   - **Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows:**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o backend Flask:
   ```bash
   python app.py
   ```

O backend estará disponível em `http://127.0.0.1:5000` por padrão.

### Frontend

1. Navegue até o diretório `frontend`:
   ```bash
   cd frontend
   ```

2. Instale as dependências:
   ```bash
   npm install
   ```

3. Inicie o servidor de desenvolvimento:
   ```bash
   npm run dev
   ```

O frontend estará disponível em `http://127.0.0.1:5173` por padrão.

---

## Endpoints da API

### Endpoints do Backend

1. **Upload de Documento**
   - **POST** `/api/upload`
   - Descrição: Aceita arquivos PDF ou TXT para processamento.

2. **Processar URL**
   - **POST** `/api/process-url`
   - Descrição: Processa a URL fornecida e retorna os dados analisados.

3. **Web Scraping**
   - **POST** `/api/scrape`
   - Descrição: Realiza web scraping recursivo na URL fornecida.

---

## Executando Testes

Para testar o backend:
```bash
pytest
```

Para testar o frontend:
```bash
npm run test
```

---

## Solução de Problemas

- **Módulo Flask Ausente:** Certifique-se de que o ambiente virtual está ativado antes de instalar as dependências.
- **Problemas de Build no Frontend:** Exclua `node_modules` e reinstale:
  ```bash
  rm -rf node_modules package-lock.json
  npm install
  ```
- **Erros no Backend:** Verifique se as dependências estão instaladas e se a versão correta do Python está sendo usada.

---

## Licença

Este projeto está licenciado sob a Licença MIT.

---

## Contribuidores

- [Lila Rodrigues](https://github.com/Lilarodrigues85)

Sinta-se à vontade para fazer fork e contribuir com este projeto!

