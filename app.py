import streamlit as st
import pickle

# Model & Vectorizer Load
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except:
    st.error("Error: Model files not found!")

st.set_page_config(page_title="ShieldAI Live", page_icon="🛡️")

# Force-fixing Button Text and Cursor
st.markdown("""
    <style>
    /* Background and Main Text */
    .stApp { background-color: #ffffff !important; }
    h1, p, label { color: #000000 !important; font-weight: bold !important; }

    /* Input Box: Black Text and Black Cursor */
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        caret-color: #000000 !important; /* Point/Cursor visibility */
        border: 2px solid #000000 !important;
    }

    /* THE ULTIMATE BUTTON FIX: Force Text Visibility */
    div.stButton > button {
        background-color: #000000 !important;
        color: #ffffff !important; /* Force text color white */
        width: 100% !important;
        height: 50px !important;
        border-radius: 5px !important;
        border: none !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }

    /* Isse text har haal mein dikhega */
    div.stButton > button p {
        color: #ffffff !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }
    
    div.stButton > button:hover {
        background-color: #333333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# UI Setup
st.title("🛡️ SHIELDAI: SECURITY SCANNER")
st.write("Professional Spam Detection System — Designed by Pritam Dash")

input_sms = st.text_area("ANALYZE MESSAGE CONTENT", placeholder="Paste suspicious text here...", height=150)

# Button with explicit text
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
