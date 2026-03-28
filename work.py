import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

gen_ai.configure(api_key=GOOGLE_API_KEY)

# ✅ Use this model
model = gen_ai.GenerativeModel("models/gemini-1.5-flash")

chat = model.start_chat(history=[])

user_input = st.text_input("Ask something:")

if user_input:
    response = chat.send_message(user_input)
    st.write(response.text)