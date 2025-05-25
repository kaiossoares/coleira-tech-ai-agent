import os
from openai import OpenAI

# Verificar se a chave está definida
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Erro: A variável de ambiente 'OPENAI_API_KEY' não está definida ou está vazia.")
else:
    print(f"OPENAI_API_KEY carregada com sucesso: {api_key[:5]}...")  # Mostra os primeiros caracteres por segurança

openai_client = OpenAI(api_key=api_key)


class RagService:
    def __init__(self, embedding_store):
        self.embedding_store = embedding_store

    def ask(self, query):
        best_doc = self.embedding_store.find_best_document(query)

        prompt = (
            f"Você é um assistente virtual que ajuda os usuários a encontrar informações sobre a Coleira Tech. "
            f"Se baseie apenas nesse documento: {best_doc['text']}. "
            f"Responda a pergunta: {query}"
        )

        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt}
            ]
        )

        return response.choices[0].message.content
