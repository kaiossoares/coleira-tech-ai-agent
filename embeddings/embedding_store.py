from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.core.node_parser import SentenceWindowNodeParser
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core.prompts import PromptTemplate
from llama_index.core.node_parser import CodeSplitter

class EmbeddingStore:
    def __init__(self):
        print("Carregando documentos...")
        documents = SimpleDirectoryReader(
            input_dir="coleira-tech-api/src/main/java/com/coleiratech/Coleira/Tech",
            recursive=True,
            required_exts=[".java", ".md", ".txt"]
        ).load_data()

        print(f"{len(documents)} documentos carregados.")

        print("Quebrando em pedaços menores...")
        parser = CodeSplitter(
            language="java",
            chunk_lines=40
        )
        nodes = parser.get_nodes_from_documents(documents)

        print("Criando embeddings...")
        embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

        print("Conectando com OpenAI...")
        llm = OpenAI(model="gpt-4o")

        print("Aplicando configurações globais...")
        Settings.llm = llm
        Settings.embed_model = embed_model

        print("Gerando índice vetorial...")
        self.index = VectorStoreIndex(nodes)

    def get_index(self):
        return self.index

    def get_query_engine(self):
        prompt = PromptTemplate(
            """
            Você é um assistente especializado em ler códigos Java da API Coleira Tech.

            Responda à pergunta utilizando **apenas** as informações dos documentos fornecidos abaixo.

            Busque por declarações de funções, métodos, classes e seus comportamentos.

            Se não encontrar a resposta, diga: "Informação não encontrada nos documentos".

            Contexto dos documentos:
            -------------------------
            {context_str}
            -------------------------

            Pergunta: {query_str}

            Resposta:
            """
        )

        return self.index.as_query_engine(
            similarity_top_k=5,
            text_qa_template=prompt
        )
