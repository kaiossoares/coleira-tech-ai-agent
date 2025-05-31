from flask import request
import streamlit as st
import requests

st.set_page_config(page_title="Coleira Chatbot", layout="wide")

st.title("Coleira Tech Chatbot")

question = st.text_input("Digite sua pergunta:")

if st.button("Enviar"):
    if question:
        response = requests.post("http://localhost:5000/query", json={"question": question})
        
        if response.status_code == 200:
            st.write(response.json().get("response"))
        else:
            st.write("Erro ao obter resposta do servidor.")
    else:
        st.write("Por favor, insira uma pergunta.")