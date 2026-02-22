import streamlit as st
from services.gemini_service import generate_response
from services.memory_service import initialize_memory, add_message, get_history
from services.profile_service import collect_profile
from prompts.prompt_templates import build_prompt

st.set_page_config(page_title="AI Financial Advisor", layout="wide")
st.title("💰 AI Financial Advisor Chatbot")

initialize_memory()
profile = collect_profile()

user_input = st.chat_input("Ask your financial question...")

if user_input:
    add_message("User", user_input)

    with st.spinner("Analyzing your financial data..."):
        prompt = build_prompt(user_input, get_history(), profile)
        response = generate_response(prompt)

    add_message("Assistant", response)

for msg in get_history():
    if msg["role"] == "User":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])