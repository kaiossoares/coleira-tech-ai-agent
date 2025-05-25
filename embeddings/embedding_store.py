from sentence_transformers import SentenceTransformer, util

class EmbeddingStore:
    def __init__(self):
        self.documents = [
            {"id": 1, "text": "A Coleira Tech, é a coleira mais inteligente do mundo, com GPS, monitoramento de saúde e muito mais."},
            {"id": 2, "text": "A API da Coleira Tech foi feita em Java com Spring Boot, com estrutura MVC."},
            {"id": 3, "text": "O grupo Coleira Tech escolheu uma Ong que foi a Gaar Campinas, que trabalha principalmente em Barão Geraldo. A Gaar Campinas auxílio o projeto com instruções sobre como fazer o projeto e também com a parte de marketing."},
        ]
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.doc_embeddings = {
            doc["id"]: self.model.encode(doc["text"], convert_to_tensor=True)
            for doc in self.documents
        }

    def find_best_document(self, query):
        query_embedding = self.model.encode(query, convert_to_tensor=True)

        best_doc = None
        best_score = float("-inf")

        for doc in self.documents:
            score = util.cos_sim(query_embedding, self.doc_embeddings[doc["id"]])
            if score > best_score:
                best_score = score
                best_doc = doc

        return best_doc
