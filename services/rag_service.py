from embeddings.embedding_store import EmbeddingStore

class RagService:
    def __init__(self, embedding_store: EmbeddingStore):
        print("Inicializando RAG Service...")
        self.embedding_store = embedding_store
        self.query_engine = self.embedding_store.get_index().as_query_engine()

    def query(self, question):
        print(f"Pergunta recebida: {question}")
        response = self.query_engine.query(question)
        return str(response)