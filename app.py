import streamlit as st
import pickle

# Model & Vectorizer Load
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except:
    st.error("Error: Model files not found!")

st.set_page_config(page_title="ShieldAI Live", page_icon="🛡️", layout="centered")

# Sab kuch force-fix karne ke liye High-Priority CSS
st.markdown("""
    <style>
    /* 1. Pure White Background for the whole app */
    .stApp {
        background-color: white !important;
    }

    /* 2. Fix all text visibility (Black/Blue) */
    h1, h2, h3, p, label, .stMarkdown, .stText {
        color: #1a5276 !important;
        font-family: 'sans-serif';
    }

    /* 3. The Ultimate Button Fix (Force White Text) */
    div.stButton > button {
        background-color: #1a5276 !important;
        color: #ffffff !important; /* Force white text */
        border-radius: 10px !important;
        width: 100% !important;
        height: 55px !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        border: none !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2) !important;
    }
    
    /* Ensure text stays white even on hover */
    div.stButton > button:hover, div.stButton > button:active, div.stButton > button:focus {
        color: #ffffff !important;
        background-color: #2471a3 !important;
        border: none !important;
    }

    /* 4. Text Area Fix (Black Cursor and Black Text) */
    .stTextArea textarea {
        background-color: #f8f9fa !important;
        color: #000000 !important;
        caret-color: #ff0000 !important; /* Bright
