import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="Chat With Harsh AI",
    page_icon="🧠",
    layout="centered",
)

# Get API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("Please set GOOGLE_API_KEY in your .env file")
    st.stop()

# Configure Gemini
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel("gemini-1.5-flash")

# Translate roles
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    return user_role

# Initialize session state
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Title
st.title("Chat With Harsh AI")

# Display chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# User input
user_prompt = st.chat_input("Ask me anything...")

if user_prompt:
    # Show user message
    st.chat_message("user").markdown(user_prompt)

    # Send to Gemini
    response = st.session_state.chat_session.send_message(user_prompt)

    # Show response
    with st.chat_message("assistant"):
        st.markdown(response.text)



