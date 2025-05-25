from flask import Flask
from flask_smorest import Api

from embeddings.embedding_store import EmbeddingStore
from services.rag_service import RagService
from controllers.rag_controller import create_rag_controller

app = Flask(__name__)
app.config["API_TITLE"] = "Coleira Tech RAG API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"

api = Api(app)

embedding_store = EmbeddingStore()
rag_service = RagService(embedding_store)

rag_controller = create_rag_controller(rag_service)
api.register_blueprint(rag_controller)

if __name__ == "__main__":
    app.run(debug=True)
