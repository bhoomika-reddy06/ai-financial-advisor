import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    try:
        GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    except Exception:
        raise ValueError("GEMINI_API_KEY not found in environment or Streamlit secrets.")

MODEL_NAME = os.getenv("MODEL_NAME") or "gemini-2.5-flash"