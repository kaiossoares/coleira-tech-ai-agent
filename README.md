# Coleira Tech AI Agent

O **Coleira Tech AI Agent** é um agente de IA projetado para auxiliar novos desenvolvedores na manutenção e evolução da [API da Coleira Tech](https://github.com/leandro-nnogueira/coleira-tech-api). Ele utiliza técnicas de Recuperação Aumentada por Geração (RAG), processamento de linguagem natural e embeddings para responder perguntas e fornecer informações relevantes sobre o projeto.

## Funcionalidades

- **Chatbot interativo** para dúvidas sobre o código da API Coleira Tech.
- Respostas baseadas no código-fonte real, utilizando embeddings e modelos de linguagem.
- Interface web simples via Streamlit.
- API REST para integração com outros sistemas.

## Estrutura do Projeto

```
coleira-tech-ai-agent/
│
├── main.py                      # Inicialização da API Flask
├── controllers/
│   └── rag_controller.py        # Controller dos endpoints RAG
├── embeddings/
│   └── embedding_store.py       # Lógica de embeddings e indexação dos arquivos da API
├── services/
│   └── rag_service.py           # Serviço de consulta RAG
├── web/
│   └── app.py                   # Interface web (Streamlit)
├── requirements.txt             # Dependências do projeto
└── README.md
```

## Pré-requisitos

- Python 3.10 ou superior
- [Coleira Tech API](https://github.com/leandro-nnogueira/coleira-tech-api) clonada na mesma estrutura de pastas
- Chave de API da OpenAI (adicione ao arquivo `.env` como `OPENAI_API_KEY`)
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone este repositório:
    ```sh
    git clone https://github.com/seu-usuario/coleira-tech-ai-agent.git
    cd coleira-tech-ai-agent
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure sua chave OpenAI no arquivo `.env`:
    ```
    OPENAI_API_KEY=sk-...
    ```

## Como rodar

### 1. Inicie a API Flask

```sh
python main.py
```

A API estará disponível em `http://localhost:5000`.

### 2. Inicie a interface web (opcional)

```sh
streamlit run web/app.py
```

Acesse a interface em `http://localhost:8501`.    