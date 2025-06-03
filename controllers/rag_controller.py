from flask_smorest import Blueprint  
from flask import request, jsonify
from services.rag_service import RagService

def create_rag_controller(rag_service: RagService):
    rag_blueprint = Blueprint("rag", __name__, description="RAG-related operations")  

    @rag_blueprint.route("/query", methods=["POST"])
    @rag_blueprint.response(200, description="Query response")  
    def query():
        data = request.get_json()
        question = data.get("question", "")
        if not question:
            return jsonify({"error": "Missing question"}), 400

        response = rag_service.query(question)
        return jsonify({"response": response})

    return rag_blueprint