from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI


class EmbeddingStore:
    def __init__(self):
        print("Carregando documentos...")
        documents = SimpleDirectoryReader("coleira-tech-api").load_data()

        print("Criando embeddings...")
        embed_model = HuggingFaceEmbedding(model_name="all-MiniLM-L6-v2")

        print("Conectando com OpenAI...")
        llm = OpenAI(model="gpt-3.5-turbo")  # ou "gpt-4"

        print("Aplicando configurações globais...")
        Settings.llm = llm
        Settings.embed_model = embed_model

        print("Gerando índice vetorial...")
        self.index = VectorStoreIndex.from_documents(documents)

    def get_index(self):
        return self.index