import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://backend:8000/query")


def main():
    st.set_page_config(page_title="MedAI Chatbot", page_icon="💬", layout="wide")
    st.markdown(
        """
        <style>
        .stChatMessage {
            background-color: #2c3e50;
            color: #ecf0f1;
            border-radius: 10px;
            padding: 5px 10px;
            margin: 10px 0;
            display: inline-block;
            max-width: 70%;
        }
        .stChatMessageUser {
            background-color: #1abc9c;
            color: #ecf0f1;
            border-radius: 10px;
            padding: 5px 10px;
            margin: 10px 0;
            display: inline-block;
            max-width: 70%;
            text-align: right;
            float: right;
        }
        .stChatMessageAssistant {
            background-color: #34495e;
            color: #ecf0f1;
            border-radius: 10px;
            padding: 5px 10px;
            margin: 10px 0;
            display: inline-block;
            max-width: 70%;
            text-align: left;
            float: left;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.title("💬 MedAI Chatbot")

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        role_class = 'stChatMessageUser' if message['role'] == 'user' else 'stChatMessageAssistant'
        st.markdown(f"<div class='{role_class}'>{message['content']}</div>", unsafe_allow_html=True)

    prompt = st.chat_input("Pass your prompt here")

    if prompt:
        st.markdown(f"<div class='stChatMessageUser'>{prompt}</div>", unsafe_allow_html=True)
        st.session_state.messages.append({'role': 'user', 'content': prompt})

        response = requests.post("http://backend:8000/query", json={"question": prompt})
        result = response.json().get("answer")

        st.markdown(f"<div class='stChatMessageAssistant'>{result}</div>", unsafe_allow_html=True)
        st.session_state.messages.append({'role': 'assistant', 'content': result})

if __name__ == "__main__":
    main()