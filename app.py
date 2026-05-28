import streamlit as st
import pickle

# Model & Vectorizer Load
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except:
    st.error("Error: Model files not found!")

st.set_page_config(page_title="ShieldAI Live", page_icon="🛡️", layout="centered")

# Black and White Minimalist Theme
st.markdown("""
    <style>
    /* 1. Background White */
    .stApp {
        background-color: #ffffff !important;
    }

    /* 2. All Text to Pure Black */
    h1, h2, h3, p, label, .stMarkdown, .stText, span {
        color: #000000 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }

    /* 3. Text Area - Black Border, Black Text, Black Cursor */
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        caret-color: #000000 !important; /* This makes the cursor BLACK */
        border: 2px solid #000000 !important;
        font-size: 16px !important;
    }

    /* 4. Button - Solid Black with White Text */
    div.stButton > button {
        background-color: #000000 !important;
        color: #ffffff !important;
        border-radius: 5px !important;
        width: 100% !important;
        height: 50px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border: 2px solid #000000 !important;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background-color: #333333 !important;
        color: #ffffff !important;
    }

    /* 5. Hide Streamlit Branding for Clean Look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Dashboard UI
st.title("🛡️ SHIELDAI: SECURITY SCANNER")
st.write("Professional Spam Detection System — Designed by Pritam Dash")

# Input area
input_sms = st.text_area("ANALYZE MESSAGE CONTENT", placeholder="Paste suspicious text here...", height=150)

# Execution Logic
if st.button('RUN DEEP SCAN'):
    if input_sms:
        vector_input = tfidf.transform([input_sms])
        result = model.predict(vector_input)[0]
        proba = model.predict_proba(vector_input)[0]
        confidence = max(proba) * 100

        if result == 1:
            st.error(f"🚨 SPAM DETECTED! (Confidence: {confidence:.2f}%)")
        else:
            st.success(f"✅ VERIFIED SAFE (Confidence: {confidence:.2f}%)")
    else:
        st.info("Please enter a message to scan.")
