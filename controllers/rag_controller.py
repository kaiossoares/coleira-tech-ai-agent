from flask_smorest import Blueprint, abort
from flask import request
from models.query_request import QueryRequest

def create_rag_controller(rag_service):
    # Use o Blueprint do Flask-Smorest
    blp = Blueprint("rag", __name__, url_prefix="/rag")

    @blp.route("/query", methods=["POST"])
    def query_rag():
        query_data = request.get_json()
        if not query_data or "query" not in query_data:
            abort(400, message="Missing 'query' field in request body")

        try:
            query_request = QueryRequest(**query_data)
        except Exception as e:
            abort(400, message=f"Invalid request format: {e}")

        try:
            response = rag_service.ask(query_request.query)
            return {"response": response}
        except Exception as e:
            abort(500, message=f"Error processing the request: {e}")

    return blp